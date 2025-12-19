import pygame
import Others
import Constantes as k


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

    # INICIALIZA O OBJETO EM UM MODO E POSIÇÃO, COM UM PERÍODO DE ANIMAÇÃO
    def set_animation(self, mode, position, period):
        self.current_mode = mode
        self.period = period
        self.current_sprite = 0
        self.sprite_count = 0
        self.image = self.sprites[self.current_mode][int(self.current_sprite)]
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    # CRIA UMA LISTA DE SPRITES PARA UM DADO MODO DO OBJETO
    def set_sprites(self, mode, sprites):
        self.sprites[mode] = sprites

    def set_mode(self, mode):
        self.current_mode = mode

    # RETORNA A POSIÇÃO DO SPRITE NA TELA
    def get_position(self):
        return self.rect.topleft

    # DEFINE A POSIÇÃO DO SPRITE NA TELA
    def set_position(self, position):
        self.rect.topleft = position

    # ATUALIZA O SPRITE DO OBJETO
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
        self.facing = 0
        self.facing_sprites_names = []
        self.digging = False
        self.damaged = False
        self.score = 0
        self.multiplier = 1
        self.max_lives = k.MIAUSMA_LIVES
        self.lives = k.MIAUSMA_LIVES
        self.max_flags = k.MIAUSMA_FLAGS
        self.flags = k.MIAUSMA_FLAGS

    def bind_facing_sprites(self, names):
        self.facing_sprites_names = names

    def face(self, side):
        if self.digging and self.current_sprite == len(self.sprites[self.current_mode]) - 1:
            self.digging = False
        if side != self.facing and not self.digging and not self.damaged:
            self.facing = side
            mode = self.facing_sprites_names[side]
            self.set_animation(mode, self.rect.topleft, self.period)

    def score_points(self, points):
        self.score += points * self.multiplier

    def increment_multiplier(self):
        self.multiplier += 1

    def damage(self, value):
        self.damaged = True
        self.lives -= value
        if self.lives <= 0:
            post_event = pygame.event.Event(k.GAME_OVER)
            pygame.event.post(post_event)

    def heal(self, value):
        self.lives += value
        if self.lives > self.max_lives:
            self.lives = self.max_lives
            post_event = pygame.event.Event(k.OVERHEAL)
            pygame.event.post(post_event)

    def flag_up(self, value):
        self.flags += value
        if self.flags > self.max_flags:
            self.flags = self.max_flags
            post_event = pygame.event.Event(k.OVERFLAG)
            pygame.event.post(post_event)

    def flag_down(self, value):
        self.flags -= value

    def wake(self):
        self.damaged = False

    # MOVIMENTAÇÃO DO PLAYER, DEVE SER CHAMADA NO LOOP PRINCIPAL DO PROGRAMA
    def move(self, directions=(False, False, False, False)):

        if self.damaged:
            self.acceleration = 0
        else:
            self.acceleration = k.MIAUSMA_ACC

        # VELOCIDADE NO EIXO X
        x_speed = self.current_speed[0]

        # PLAYER NÃO PODE PASSAR DA VELOCIDADE MÁXIMA (EIXO X)
        if abs(x_speed) > self.max_speed:
            self.current_speed[0] = self.max_speed * (-1 + 2 * (x_speed > 0))

        # ACELERA PARA A ESQUERDA
        if directions[0]:
            self.current_speed[0] -= self.acceleration
        # ACELERA PARA A DIREITA
        if directions[1]:
            self.current_speed[0] += self.acceleration

        # DESACELERA QUANDO NÃO HÁ INPUT (EIXO X)
        if not (directions[0] or directions[1]) and abs(x_speed) > self.critical_damp:
            self.current_speed[0] += self.dampen * (-1 + 2 * (x_speed < 0))
        # PARA TOTALMENTE QUANDO ATINGE UM LIMITE CRÍTICO DE VELOCIDADE (EIXO X)
        if not (directions[0] or directions[1]) and abs(x_speed) <= self.critical_damp:
            self.current_speed[0] = 0

        # MOVIMENTA O PLAYER NO EIXO X
        x_speed = self.current_speed[0]
        self.rect.x += x_speed

        # VELOCIDADE NO EIXO Y
        y_speed = self.current_speed[1]

        # PLAYER NÃO PODE PASSAR DA VELOCIDADE MÁXIMA (EIXO Y)
        if abs(y_speed) > self.max_speed:
            self.current_speed[1] = self.max_speed * (-1 + 2 * (y_speed > 0))

        # ACELERA PARA CIMA
        if directions[2]:
            self.current_speed[1] -= self.acceleration
        # ACELERA PARA BAIXO
        if directions[3]:
            self.current_speed[1] += self.acceleration

        # DESACELERA QUANDO NÃO HÁ INPUT (EIXO Y)
        if not (directions[2] or directions[3]) and abs(y_speed) > self.critical_damp:
            self.current_speed[1] += self.dampen * (-1 + 2 * (y_speed < 0))
        # PARA TOTALMENTE QUANDO ATINGE UM LIMITE CRÍTICO DE VELOCIDADE (EIXO Y)
        if not (directions[2] or directions[3]) and abs(y_speed) <= self.critical_damp:
            self.current_speed[1] = 0

        # MOVIMENTA O PLAYER NO EIXO Y
        y_speed = self.current_speed[1]
        self.rect.y += y_speed

    def get_current_speed(self):
        return self.current_speed

    def set_current_speed(self, speed):
        self.current_speed = speed

class ButtonMask(Sprite):

    def __init__(self, button, idle_mode, hover_mode):
        super().__init__()
        self.button = button
        self.idle_mode = idle_mode
        self.hover_mode = hover_mode

    def update(self):
        Sprite.update(self)
        if self.button.idling and self.current_mode != self.idle_mode:
            self.current_mode = self.idle_mode
        if self.button.hovering and self.current_mode != self.hover_mode:
            self.current_mode = self.hover_mode

class Flag(Sprite):

    placed_flags = {}

    def __init__(self, spawn, change_mode):
        super().__init__()
        self.spawn = spawn
        self.change_mode = change_mode
        self.coordinate = None

    def update(self):
        Sprite.update(self)
        if self.spawn and self.current_sprite == len(self.sprites[self.current_mode]) - 1:
            self.spawn = False
            self.current_mode = self.change_mode

    def generate(self, position, group, layer):
        new_flag = self.__class__(True, self.change_mode)
        new_flag.sprites = self.sprites
        new_flag.set_animation(self.current_mode, position, self.period)
        group.add(new_flag, layer=layer)
        return new_flag

class Bomb(Sprite):

    def __init__(self, spawn, change_mode1, change_mode2):
        super().__init__()
        self.spawn = spawn
        self.charging = False
        self.change_mode1 = change_mode1
        self.change_mode2 = change_mode2
        self.coordinate = None

    def update(self):
        Sprite.update(self)
        if self.spawn and not self.charging and self.current_sprite == len(self.sprites[self.current_mode]) - 1:
            self.spawn = False
            self.charging = True
            self.current_mode = self.change_mode1
            self.current_sprite = 0
        if not self.spawn and self.charging and self.current_sprite == len(self.sprites[self.current_mode]) - 1:
            self.charging = False
            self.current_mode = self.change_mode2
            self.current_sprite = 0
            post_event = pygame.event.Event(k.DAMAGE_PLAYER)
            pygame.event.post(post_event)
        if not self.spawn and not self.charging and self.current_sprite == len(self.sprites[self.current_mode]) - 1:
            self.kill()

    def generate(self, position, group, layer):
        new_flag = self.__class__(True, self.change_mode1, self.change_mode2)
        new_flag.sprites = self.sprites
        new_flag.set_animation(self.current_mode, position, self.period)
        group.add(new_flag, layer=layer)
        return new_flag

class Collectable(Sprite):

    def __init__(self, player, spawn, change_mode, lifetime):
        super().__init__()
        self.player = player
        self.spawn = spawn
        self.change_mode = change_mode
        self.lifetime = lifetime
        self.timer = Others.Timer()
        self.timer.set_timer_seconds(lifetime)
        self.timer.activate()

    def update(self):
        Sprite.update(self)
        if self.spawn and self.current_sprite == len(self.sprites[self.current_mode]) - 1:
            self.spawn = False
            self.current_mode = self.change_mode
        if self.rect.collidepoint(self.player.rect.center) and not self.spawn:
            self.kill()
            self.effect()
        if self.timer.ring():
            self.kill()

    def generate(self, position, group, layer):
        new_collectable = self.__class__(self.player, True, self.change_mode, self.lifetime)
        new_collectable.sprites = self.sprites
        new_collectable.set_animation(self.current_mode, position, self.period)
        group.add(new_collectable, layer=layer)

    def effect(self):
        post_event = pygame.event.Event(k.GET_COLLECTABLE, {'caller': self})
        pygame.event.post(post_event)

class LifeCollectable(Collectable):

    def __init__(self, player, spawn, change_mode, lifetime):
        super().__init__(player, spawn, change_mode, lifetime)

class TimeCollectable(Collectable):

    def __init__(self, player, spawn, change_mode, lifetime):
        super().__init__(player, spawn, change_mode, lifetime)

class FlagCollectable(Collectable):

    def __init__(self, player, spawn, change_mode, lifetime):
        super().__init__(player, spawn, change_mode, lifetime)
