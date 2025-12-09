import pygame

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
