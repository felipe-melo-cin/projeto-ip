import pygame
import Interfaces
import Sprites
import Others
import Constantes as k
import Algoritmos

# OBJETO DO MOUSE
MOUSE = Others.Mouse()

# BOTÕES
TO_MAIN_GAME_BUTTON = Interfaces.ToMainGameButton(k.TO_MAIN_GAME_BUTTON_SIZE, k.TO_MAIN_GAME_BUTTON_POSITION, MOUSE, None)
QUIT_GAME_BUTTON = Interfaces.QuitGameButton(k.QUIT_GAME_BUTTON_SIZE, k.QUIT_GAME_BUTTON_POSITION, MOUSE)

# PARTE LÓGICA DO CAMPO MINADO
ABSTRACT_MINEFIELD = Algoritmos.AbstractMinefield((10, 10), 0.2)

# PARTE INTERAGÍVEL DO CAMPO MINADO
MINEFIELD = Interfaces.TileGrid(k.MINEFIELD_SIZE, k.MINEFIELD_POSITION, MOUSE, Interfaces.Tile, (k.MINEFIELD_SIZE[0] // 10, k.MINEFIELD_SIZE[1] // 10), ABSTRACT_MINEFIELD)

# PREENCHENDO CAMPO MINADO
MINEFIELD.fill_matrix()

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

        # ASSOCIANDO BOTÕES
        TO_MAIN_GAME_BUTTON.gsm = self.gsm

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

                    if event.button == 1: # CLIQUE COM BOTÃO ESQUERDO
                        MOUSE.set_left_click()

                    if event.button == 3: # CLIQUE COM BOTÃO DIREITO
                        MOUSE.set_right_click()

                # TERMINOU O CLIQUE COM O MOUSE
                if event.type == pygame.MOUSEBUTTONUP:

                    if event.button == 1: # CLIQUE COM BOTÃO ESQUERDO
                        MOUSE.reset_left_press()

                    if event.button == 3: # CLIQUE COM BOTÃO DIREITO
                        MOUSE.reset_right_press()

                # OBJETO DO TIMER CHEGOU A ZERO
                if event.type == k.RING_EVENT:
                    pass

            # DECIDINDO QUAL TELA ESTÁ SENDO EXECUTADA
            current_state = self.gsm.get_state()
            current_state(self.screen, self.gsm).run()

            # DESFAZ O CLIQUE INICIAL DO MOUSE
            MOUSE.reset_left_click()
            MOUSE.reset_right_click()

            # ATUALIZA O DISPLAY
            self.screen.update()

            # LIMITE DA TAXA DE QUADROS
            self.clock.tick(self.FPS)

class GameStateManager:

    def __init__(self):
        # INICIALIZA O OBJETO DO GERENCIADOR
        self.states = {}
        self.current_state = None

    def create_state(self, state_bundle):
        # CRIA UMA SÉRIE DE ESTADOS PARA O GERENCIADOR
        self.states[state_bundle[0]] = state_bundle[1]

    def set_state(self, state):
        # DEFINE O ESTADO ATUAL DO GERADOR
        self.current_state = self.states[state]

    def get_state(self):
        # RETORNA A CLASSE CORRESPONDENTE AO ESTADO DO GERENCIADOR
        return self.current_state

class MainMenu:

    def __init__(self, screen, gsm):
        # INICIALIZA O MENU PRINCIPAL
        self.screen = screen
        self.gsm = gsm

    def run(self):
        # INSERE OS BOTÕES NA TELA
        self.screen.put_inside(TO_MAIN_GAME_BUTTON, TO_MAIN_GAME_BUTTON.rect.topleft)
        self.screen.put_inside(QUIT_GAME_BUTTON, QUIT_GAME_BUTTON.rect.topleft)

        # CARREGA OS BOTÕES NA TELA
        TO_MAIN_GAME_BUTTON.update()
        QUIT_GAME_BUTTON.update()

class MainGame:

    def __init__(self, screen, gsm):
        # INICIA UMA RODADA DO JOGO
        self.screen = screen
        self.gsm = gsm

    def run(self):
        # INSERE O CAMPO MINADO NA TELA
        self.screen.put_inside(MINEFIELD, MINEFIELD.rect.topleft)

        # CARREGA O CAMPO MINADO NA TELA
        MINEFIELD.update()
