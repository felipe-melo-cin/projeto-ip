import pygame
from abc import ABC, abstractmethod
import Constantes as k

class Screen:

    def __init__(self):
        self.display = None
        self.size = None

    @staticmethod
    def set_title(title):
        # DEFINE O TÍTULO DA TELA
        pygame.display.set_caption(title)

    @staticmethod
    def update():
        # ATUALIZA O DISPLAY
        pygame.display.update()

    def set_size(self, size):
        # DEFINE O TAMANHO DA TELA
        self.size = size

    def show(self):
        # MOSTRA A TELA
        self.display = pygame.display.set_mode(self.size)

    def fill(self, color):
        # PREENCHE A TELA COM UMA COR
        self.display.fill(color)

    def put_inside(self, asset, position):
        # INSERE UM ASSET GRÁFICO NA TELA
        self.display.blit(asset, position)

class Button(ABC, pygame.surface.Surface):

    def __init__(self, size, position, mouse):
        super().__init__(size)
        self.left_pressed = None
        self.right_pressed = None
        self.rect = self.get_rect()
        self.rect.topleft = position
        self.MOUSE = mouse

    # CHECAGEM DE ESTADO DO BOTÃO
    def update(self):

        # MOUSE ESTÁ OU NÃO NA TELA
        if not pygame.mouse.get_focused():
            mouse_collide = False
        else:
            mouse_collide = self.rect.collidepoint(self.MOUSE.position)

        # MOUSE NÃO COLIDE COM O BOTÃO
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
        for buffer in self.button_matrix:
            for button in buffer:
                button_x, button_y = button.rect.topleft
                self.put_inside(button, (button_x - offset_x, button_y - offset_y))
                button.update()

    def fill_matrix(self):
        offset_x, offset_y = self.rect.topleft
        fill_pointer_x, fill_pointer_y = (0, 0)

        while fill_pointer_y + self.button_height <= self.height:
            x_buffer = []
            while fill_pointer_x + self.button_width <= self.width:
                x_buffer.append(self.button_type((self.button_width, self.button_height), (fill_pointer_x + offset_x, fill_pointer_y + offset_y), self.MOUSE))
                fill_pointer_x += self.button_width

            self.button_matrix.append(x_buffer.copy())
            x_buffer.clear()

            fill_pointer_x = 0
            fill_pointer_y += self.button_height

class TileGrid(ButtonGrid):

    def __init__(self, size, position, mouse, button_type, button_size, minefield):
        super().__init__(size, position, mouse, button_type, button_size)
        self.button_type = Tile
        self.minefield = minefield
        self.minefield.fill_minefield()

    def update(self):
        offset_x, offset_y = self.rect.topleft
        for buffer in self.button_matrix:
            for button in buffer:
                button_x, button_y = button.rect.topleft
                self.put_inside(button, (button_x - offset_x, button_y - offset_y))
                button.update()

    def fill_matrix(self):
        offset_x, offset_y = self.rect.topleft
        fill_pointer_x, fill_pointer_y = (0, 0)

        i_counter = 0
        while fill_pointer_y + self.button_height <= self.height:
            x_buffer = []
            j_counter = 0
            while fill_pointer_x + self.button_width <= self.width:
                x_buffer.append(self.button_type((self.button_width, self.button_height), (fill_pointer_x + offset_x, fill_pointer_y + offset_y), self.MOUSE, self.minefield, (i_counter, j_counter)))
                fill_pointer_x += self.button_width
                j_counter += 1

            self.button_matrix.append(x_buffer.copy())
            x_buffer.clear()
            i_counter += 1

            fill_pointer_x = 0
            fill_pointer_y += self.button_height

class ToMainGameButton(Button):

    def __init__(self, size, position, mouse, gsm):
        super().__init__(size, position, mouse)
        self.gsm = gsm

    def main_action(self):
        self.gsm.set_state('main game')

    def side_action(self):
        pass

    def idle(self):
        self.fill('white')

    def hover(self):
        self.fill('gray')

    def main_press(self):
        self.fill('black')

    def side_press(self):
        pass

class QuitGameButton(Button):

    def __init__(self, size, position, mouse):
        super().__init__(size, position, mouse)

    def main_action(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    def side_action(self):
        pass

    def idle(self):
        self.fill('crimson')

    def hover(self):
        self.fill('dark red')

    def main_press(self):
        self.fill('black')

    def side_press(self):
        pass

class Tile(Button):

    def __init__(self, size, position, mouse, minefield, coordinates):
        super().__init__(size, position, mouse)
        self.minefield = minefield
        self.coordinates = coordinates
        self.i, self.j = coordinates
        self.code = 10

    def update(self):
        Button.update(self)
        minefield_tile = self.minefield.minefield[self.i][self.j]
        if self.minefield.minefield_mask[0]:
            mask_tile = self.minefield.minefield_mask[self.i][self.j]
        interface_tile = self.minefield.minefield_interface[self.i][self.j]

        if interface_tile == 0:
            self.code = 10
        elif interface_tile == 2:
            self.code = 11
        elif minefield_tile:
            self.code = 9
        else:
            self.code = mask_tile

    def draw_line(self, color, mod_a, mod_b):
        rect = self.get_rect()
        bottom = rect.bottom
        right = rect.right
        mod_ai, mod_aj = mod_a
        mod_bi, mod_bj = mod_b
        pygame.draw.line(self, color, (right * mod_aj, bottom * mod_ai), (right * mod_bj, bottom * mod_bi), k.NUMBER_WIDTH)

    def draw_number(self, number):
        if number == 1:
            self.draw_line(k.COLOR_BLUE, (0.25, 0.25), (0.25, 0.5))
            self.draw_line(k.COLOR_BLUE, (0.25, 0.5), (0.75, 0.5))
            self.draw_line(k.COLOR_BLUE, (0.75, 0.25), (0.75, 0.75))
        elif number == 2:
            self.draw_line(k.COLOR_GREEN, (0.25, 0.25), (0.25, 0.75))
            self.draw_line(k.COLOR_GREEN, (0.25, 0.75), (0.5, 0.75))
            self.draw_line(k.COLOR_GREEN, (0.5, 0.75), (0.5, 0.25))
            self.draw_line(k.COLOR_GREEN, (0.5, 0.25), (0.75, 0.25))
            self.draw_line(k.COLOR_GREEN, (0.75, 0.25), (0.75, 0.75))
        elif number == 3:
            self.draw_line(k.COLOR_RED, (0.25, 0.25), (0.25, 0.75))
            self.draw_line(k.COLOR_RED, (0.5, 0.25), (0.5, 0.75))
            self.draw_line(k.COLOR_RED, (0.75, 0.25), (0.75, 0.75))
            self.draw_line(k.COLOR_RED, (0.25, 0.75), (0.75, 0.75))
        elif number == 4:
            self.draw_line(k.COLOR_DARK_BLUE, (0.25, 0.25), (0.5, 0.25))
            self.draw_line(k.COLOR_DARK_BLUE, (0.5, 0.25), (0.5, 0.75))
            self.draw_line(k.COLOR_DARK_BLUE, (0.25, 0.75), (0.75, 0.75))
        elif number == 5:
            self.draw_line(k.COLOR_MAROON, (0.25, 0.25), (0.25, 0.75))
            self.draw_line(k.COLOR_MAROON, (0.25, 0.25), (0.5, 0.25))
            self.draw_line(k.COLOR_MAROON, (0.5, 0.75), (0.5, 0.25))
            self.draw_line(k.COLOR_MAROON, (0.5, 0.75), (0.75, 0.75))
            self.draw_line(k.COLOR_MAROON, (0.75, 0.25), (0.75, 0.75))
        elif number == 6:
            self.draw_line(k.COLOR_TEAL, (0.25, 0.25), (0.25, 0.75))
            self.draw_line(k.COLOR_TEAL, (0.25, 0.25), (0.75, 0.25))
            self.draw_line(k.COLOR_TEAL, (0.5, 0.75), (0.5, 0.25))
            self.draw_line(k.COLOR_TEAL, (0.5, 0.75), (0.75, 0.75))
            self.draw_line(k.COLOR_TEAL, (0.75, 0.25), (0.75, 0.75))
        elif number == 7:
            self.draw_line(k.COLOR_DARK_GRAY, (0.25, 0.25), (0.25, 0.75))
            self.draw_line(k.COLOR_DARK_GRAY, (0.25, 0.75), (0.75, 0.75))
        elif number == 8:
            self.draw_line(k.COLOR_GRAY, (0.25, 0.25), (0.25, 0.75))
            self.draw_line(k.COLOR_GRAY, (0.5, 0.25), (0.5, 0.75))
            self.draw_line(k.COLOR_GRAY, (0.75, 0.25), (0.75, 0.75))
            self.draw_line(k.COLOR_GRAY, (0.25, 0.25), (0.75, 0.25))
            self.draw_line(k.COLOR_GRAY, (0.25, 0.75), (0.75, 0.75))

    def main_action(self):
        self.minefield.dig(self.coordinates)

    def side_action(self):
        if self.code == 10:
            self.minefield.minefield_interface[self.i][self.j] = 2
        elif self.code == 11:
            self.minefield.minefield_interface[self.i][self.j] = 0

    def idle(self):
        if self.code == 10:
            self.fill(k.COLOR_PURPLE)
            pygame.draw.rect(self, k.COLOR_DARK_PURPLE, self.get_rect(), k.TILE_WIDTH)
        elif self.code == 11:
            self.fill(k.COLOR_RED)
            pygame.draw.rect(self, k.COLOR_DARK_RED, self.get_rect(), k.TILE_WIDTH)
        elif self.code == 9:
            pass
        else:
            self.fill(k.COLOR_YELLOW)
            pygame.draw.rect(self, k.COLOR_DARK_YELLOW, self.get_rect(), k.TILE_WIDTH)
            self.draw_number(self.code)

    def hover(self):
        if self.code == 10:
            self.fill(k.COLOR_DARK_PURPLE)
            pygame.draw.rect(self, k.COLOR_DARK_PURPLE, self.get_rect(), k.TILE_WIDTH)
        elif self.code == 11:
            self.fill(k.COLOR_DARK_RED)
            pygame.draw.rect(self, k.COLOR_DARK_RED, self.get_rect(), k.TILE_WIDTH)
        elif self.code == 9:
            pass
        else:
            self.fill(k.COLOR_YELLOW)
            pygame.draw.rect(self, k.COLOR_DARK_YELLOW, self.get_rect(), k.TILE_WIDTH)
            self.draw_number(self.code)

    def main_press(self):
        self.hover()

    def side_press(self):
        self.hover()
