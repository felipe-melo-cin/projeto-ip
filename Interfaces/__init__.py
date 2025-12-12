import pygame
from abc import ABC, abstractmethod

class Screen:

    def __init__(self):
        self.display = None
        self.size = None

    @staticmethod
    def set_title(title):
        pygame.display.set_caption(title)

    @staticmethod
    def update():
        pygame.display.update()

    def set_size(self, size):
        self.size = size

    def show(self):
        self.display = pygame.display.set_mode(self.size)

    def fill(self, color):
        self.display.fill(color)

    def put_inside(self, asset, position):
        self.display.blit(asset, position)

class Button(ABC, pygame.surface.Surface):

    def __init__(self, size, position, mouse):
        super().__init__(size)
        self.left_pressed = None
        self.right_pressed = None
        self.rect = self.get_rect()
        self.rect.topleft = position
        self.MOUSE = mouse

    def update(self):

        if not pygame.mouse.get_focused():
            mouse_collide = False
        else:
            mouse_collide = self.rect.collidepoint(self.MOUSE.position)

        if not mouse_collide:
            self.left_pressed = False
            self.right_pressed = False
            self.idle()
        elif mouse_collide and not self.MOUSE.left_click and not self.left_pressed and not self.MOUSE.right_click and not self.right_pressed:
            self.left_pressed = False
            self.right_pressed = False
            self.hover()

        elif mouse_collide and not self.MOUSE.left_press and self.left_pressed:
            self.left_pressed = False
            self.idle()
            self.main_action()
        elif mouse_collide and not self.MOUSE.right_press and self.right_pressed:
            self.right_pressed = False
            self.idle()
            self.side_action()

        elif mouse_collide and (self.MOUSE.left_click or self.left_pressed) and not self.right_pressed:
            self.left_pressed = True
            self.main_press()
        elif mouse_collide and (self.MOUSE.right_click or self.right_pressed) and not self.left_pressed:
            self.right_pressed = True
            self.side_press()

    @abstractmethod
    def main_action(self):
        pass

    def side_action(self):
        pass

    @abstractmethod
    def idle(self):
        pass

    @abstractmethod
    def hover(self):
        pass

    @abstractmethod
    def main_press(self):
        pass

    def side_press(self):
        pass

class ButtonGrid(pygame.surface.Surface):

    def __init__(self, size, position, mouse, button_type, button_size):
        super().__init__(size)
        self.rect = self.get_rect()
        self.rect.topleft = position
        self.MOUSE = mouse
        self.width, self.height = size
        self.button_type = button_type
        self.button_width, self.button_height = button_size
        self.button_matrix = []

    def put_inside(self, button, position):
        self.blit(button, position)

    def update(self):
        offset_x, offset_y = self.rect.topleft
        for button in self.button_matrix:
            button_x, button_y = button.rect.topleft
            self.put_inside(button, (button_x - offset_x, button_y - offset_y))
            button.update()

    def fill_matrix(self):
        offset_x, offset_y = self.rect.topleft
        fill_pointer_x, fill_pointer_y = (0, 0)

        while fill_pointer_y + self.button_height <= self.height:

            while fill_pointer_x + self.button_width <= self.width:
                self.button_matrix.append(self.button_type((self.button_width, self.button_height), (fill_pointer_x + offset_x, fill_pointer_y + offset_y), self.MOUSE))
                fill_pointer_x += self.button_width

            fill_pointer_x = 0
            fill_pointer_y += self.button_height
