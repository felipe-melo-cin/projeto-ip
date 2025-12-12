import pygame
import MainFolder.Interfaces as Interfaces
import MainFolder.Sprites as Sprites
import MainFolder.Others as Others

# OBJETO DO MOUSE
MOUSE = Others.Mouse()

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

        # GERENCIADOR DE ESTADOS
        self.gsm = None

    def screen_init(self):
        # INICIALIZANDO A TELA INICIAL
        self.screen = Interfaces.Screen()
        self.screen.set_title(self.game_title)
        self.screen.set_size(self.screen_size)
        self.screen.show()

    def gsm_init(self, bundles, first_state):
        # INICIALIZANDO O GERENCIADOR DE ESTADOS
        self.gsm = GameStateManager()

        # CRIANDO ESTADOS
        for state_bundle in bundles:
            self.gsm.create_state(state_bundle)

        # SELECIONANDO O PRIMEIRO ESTADO
        self.gsm.set_state(first_state)

    def run(self):
        # EXECUTANDO A TELA INICIAL
        self.gsm.set_state('main menu')

        while True:
            # LOOP DE EVENTOS
            for event in pygame.event.get():

                # SAIR
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                # INICIOU O CLIQUE COM O MOUSE
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if event.button == 1:
                        MOUSE.set_left_click()

                    if event.button == 3:
                        MOUSE.set_right_click()

                # TERMINOU O CLIQUE COM O MOUSE
                if event.type == pygame.MOUSEBUTTONUP:

                    if event.button == 1:
                        MOUSE.reset_left_press()

                    if event.button == 3:
                        MOUSE.reset_right_press()

                # OBJETO DO TIMER CHEGOU A ZERO
                if event.type == Others.RING_EVENT:
                    pass

            current_state = self.gsm.get_state()
            current_state(self.screen, self.gsm).run()

            MOUSE.reset_left_click()
            MOUSE.reset_right_click()

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
