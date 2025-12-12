import pygame

RING_EVENT = pygame.event.custom_type()

class Mouse:

    def __init__(self):
        self.left_click = None
        self.left_press = None
        self.right_click = None
        self.right_press = None

    @property
    def position(self):
        return pygame.mouse.get_pos()

    def set_left_click(self):
        self.left_click = True
        self.left_press = True

    def set_right_click(self):
        self.right_click = True
        self.right_press = True

    def reset_left_click(self):
        self.left_click = False

    def reset_right_click(self):
        self.right_click = False

    def reset_left_press(self):
        self.left_press = False

    def reset_right_press(self):
        self.right_press = False

class Timer:

    def __init__(self):
        self.start_time = None
        self.time_limit = None
        self.current_time = None
        self.POST_EVENT = pygame.event.Event(RING_EVENT, {'caller': self})

    def set_timer_seconds(self, time):
        self.start_time = time * 1000

    def activate(self):
        self.time_limit = self.start_time + pygame.time.get_ticks()
        self.current_time = self.start_time

    def ring(self):
        if self.current_time > 0:
            self.current_time = self.time_limit - pygame.time.get_ticks()
        else:
            pygame.event.post(self.POST_EVENT)
