import pygame
import Constantes as k

class Mouse:

    def __init__(self):
        self.left_click = None
        self.left_press = None
        self.right_click = None
        self.right_press = None

    @property
    def position(self):
        # RETORNA A POSIÇÃO DO MOUSE
        return pygame.mouse.get_pos()

    def set_left_click(self):
        # INICIA O CLIQUE ESQUERDO DO MOUSE
        self.left_click = True
        self.left_press = True

    def set_right_click(self):
        # INICIA O CLIQUE DIREITO DO MOUSE
        self.right_click = True
        self.right_press = True

    def reset_left_click(self):
        # TERMINA O CLIQUE ESQUERDO
        self.left_click = False

    def reset_right_click(self):
        # TERMINA O CLIQUE DIREITO
        self.right_click = False

    def reset_left_press(self):
        # TERMINA O PRESSIONAMENTO DO BOTÃO ESQUERDO
        self.left_press = False

    def reset_right_press(self):
        # TERMINA O PRESSIONAMENTO DO BOTÃO DIREITO
        self.right_press = False

# UM TIMER QUE CONTA ATÉ ZERO
class Timer:

    def __init__(self):
        self.start_time = None
        self.time_limit = None
        self.current_time = None
        self.activated = False

    # PREPARA O TIMER COM UM DADO TEMPO EM SEGUNDOS
    def set_timer_seconds(self, time):
        self.start_time = time * 1000

    # ADICIONA TEMPO AO TIMER
    def add_time_seconds(self, time):
        self.time_limit += time * 1000

    def get_current_time_seconds(self):
        if self.activated:
            return self.current_time // 1000

    # ATIVA O TIMER
    def activate(self):
        self.activated = True
        self.time_limit = self.start_time + pygame.time.get_ticks()
        self.current_time = self.start_time

    # CHECA SE O TIMER ATINGIU O LIMITE DE TEMPO
    def ring(self):
        if self.activated:
            if self.current_time > 0:
                self.current_time = self.time_limit - pygame.time.get_ticks()
                return False
            else:
                self.activated = False
                self.current_time = 0
                return True
