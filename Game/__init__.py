import pygame
import MainFolder.Interfaces as Interfaces
import MainFolder.Characters as Characters

class Game:

    def __init__(self, game_title, screen_size, fps):
        # INICIALIZANDO PYGAME
        pygame.init()

        # CLOCK E TAXA DE QUADROS
        self.clock = pygame.time.Clock()
        self.FPS = fps

        # INFORMAÇÕES PARA A TELA INICIAL
        self.game_title = game_title
        self.screen_size = screen_size
        self.screen = None

        # ADMINISTRADOR DE ESTADOS
        self.gsm = None

    def screen_init(self):
        self.screen = Interfaces.Screen()
        self.screen.set_title(self.game_title)
        self.screen.set_size(self.screen_size)
        self.screen.show()

    def gsm_init(self, bundles, first_state):
        self.gsm = GameStateManager()

        for state_bundle in bundles:
            self.gsm.create_state(state_bundle)

        self.gsm.set_state(first_state)

    def run(self):

        self.gsm.set_state('main menu')

        while True:
            # LOOP DE EVENTOS
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

            current_state = self.gsm.get_state()
            current_state(self.screen, self.gsm).run()

            # ATUALIZA O DISPLAY
            self.screen.update()

            # LIMITE DA TAXA DE QUADROS
            self.clock.tick(self.FPS)

class GameStateManager:

    def __init__(self):
        self.states = {}
        self.current_state = None

    def create_state(self, state_bundle):
        self.states[state_bundle[0]] = state_bundle[1]

    def set_state(self, state):
        self.current_state = self.states[state]

    def get_state(self):
        return self.current_state

class MainMenu:

    def __init__(self, screen, gsm):
        self.screen = screen
        self.gsm = gsm

    def run(self):
        pass

class MainGame:

    def __init__(self, screen, gsm):
        self.screen = screen
        self.gsm = gsm

    def run(self):
        pass
