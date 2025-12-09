import pygame

class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.sprites = {}
        self.current_mode = None
        self.period = None
        self.current_sprite = None
        self.sprite_count = None
        self.image = None
        self.rect = None

    def set_animation(self, mode, position, period):
        self.current_mode = mode
        self.period = period
        self.current_sprite = 0
        self.sprite_count = 0
        self.image = self.sprites[self.current_mode][int(self.current_sprite)]
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def set_sprites(self, mode, sprites):
        self.sprites[mode] = sprites

    def update(self):
        self.sprite_count += 1
        if self.sprite_count >= self.period:
            self.sprite_count = 0
            self.current_sprite += 1
        self.current_sprite %= len(self.sprites[self.current_mode])
        self.image = self.sprites[self.current_mode][int(self.current_sprite)]

class Player(Sprite):

    def __init__(self, max_speed, acc, dampen, cdamp):
        super().__init__()
        self.current_speed = [0, 0]
        self.max_speed = max_speed
        self.acceleration = acc
        self.dampen = dampen
        self.critical_damp = cdamp

    def move(self, directions=(False, False, False, False)):

        x_speed = self.current_speed[0]

        if abs(x_speed) > self.max_speed:
            self.current_speed[0] = self.max_speed * (-1 + 2 * (x_speed > 0))

        if directions[0]:
            self.current_speed[0] -= self.acceleration
        if directions[1]:
            self.current_speed[0] += self.acceleration

        if not (directions[0] or directions[1]) and abs(x_speed) > self.critical_damp:
            self.current_speed[0] += self.dampen * (-1 + 2 * (x_speed < 0))
        if not (directions[0] or directions[1]) and abs(x_speed) <= self.critical_damp:
            self.current_speed[0] = 0

        x_speed = self.current_speed[0]
        self.rect.x += x_speed

        y_speed = self.current_speed[1]

        if abs(y_speed) > self.max_speed:
            self.current_speed[1] = self.max_speed * (-1 + 2 * (y_speed > 0))

        if directions[2]:
            self.current_speed[1] -= self.acceleration
        if directions[3]:
            self.current_speed[1] += self.acceleration

        if not (directions[2] or directions[3]) and abs(y_speed) > self.critical_damp:
            self.current_speed[1] += self.dampen * (-1 + 2 * (y_speed < 0))
        if not (directions[2] or directions[3]) and abs(y_speed) <= self.critical_damp:
            self.current_speed[1] = 0

        y_speed = self.current_speed[1]
        self.rect.y += y_speed
