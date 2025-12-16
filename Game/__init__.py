import pygame
import Interfaces
import Sprites
import Others
import Constantes as k
import Algoritmos
from random import randint

# OBJETO DO MOUSE
MOUSE = Others.Mouse()

# PROTAGONISTA
MIAUSMA = Sprites.Player(k.MIAUSMA_MAX_SPEED, k.MIAUSMA_ACC, k.MIAUSMA_DAMPEN, k.MIAUSMA_CDAMP)

MIAUSMA.set_sprites('idle', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/idle0.png',
    '../Images/idle1.png',
    '../Images/idle2.png',
    '../Images/idle3.png',
    '../Images/idle4.png',
    '../Images/idle5.png',
)))

MIAUSMA.set_sprites('walk up', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_up0.png',
    '../Images/walk_up1.png',
    '../Images/walk_up2.png',
    '../Images/walk_up3.png',
    '../Images/walk_up4.png',
    '../Images/walk_up5.png'
)))

MIAUSMA.set_sprites('walk down', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_down0.png',
    '../Images/walk_down1.png',
    '../Images/walk_down2.png',
    '../Images/walk_down3.png',
    '../Images/walk_down4.png',
    '../Images/walk_down5.png'
)))

MIAUSMA.set_sprites('walk left', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_left0.png',
    '../Images/walk_left1.png',
    '../Images/walk_left2.png',
    '../Images/walk_left3.png',
    '../Images/walk_left4.png',
    '../Images/walk_left5.png'
)))

MIAUSMA.set_sprites('walk right', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_right0.png',
    '../Images/walk_right1.png',
    '../Images/walk_right2.png',
    '../Images/walk_right3.png',
    '../Images/walk_right4.png',
    '../Images/walk_right5.png'
)))

MIAUSMA.set_sprites('walk down left', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_down_left0.png',
    '../Images/walk_down_left1.png',
    '../Images/walk_down_left2.png',
    '../Images/walk_down_left3.png',
    '../Images/walk_down_left4.png',
    '../Images/walk_down_left5.png'
)))

MIAUSMA.set_sprites('walk up left', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_up_left0.png',
    '../Images/walk_up_left1.png',
    '../Images/walk_up_left2.png',
    '../Images/walk_up_left3.png',
    '../Images/walk_up_left4.png',
    '../Images/walk_up_left5.png'
)))

MIAUSMA.set_sprites('walk up right', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_up_right0.png',
    '../Images/walk_up_right1.png',
    '../Images/walk_up_right2.png',
    '../Images/walk_up_right3.png',
    '../Images/walk_up_right4.png',
    '../Images/walk_up_right5.png'
)))

MIAUSMA.set_sprites('walk down right', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/walk_down_right0.png',
    '../Images/walk_down_right1.png',
    '../Images/walk_down_right2.png',
    '../Images/walk_down_right3.png',
    '../Images/walk_down_right4.png',
    '../Images/walk_down_right5.png'
)))

MIAUSMA.set_sprites('dig', k.resize_images(k.MIAUSMA_SIZE, (
    '../Images/dig0.png',
    '../Images/dig1.png',
    '../Images/dig2.png',
    '../Images/dig3.png',
    '../Images/dig4.png',
    '../Images/dig5.png'
)))

MIAUSMA.bind_facing_sprites(('idle', 'walk down', 'walk left', 'walk up', 'walk right', 'walk down left', 'walk up left', 'walk up right', 'walk down right'))
MIAUSMA.set_animation('idle', k.set_proportion(2.14, 2.24), 7)

# BANDEIRAS
FLAG_OBJECT = Sprites.Flag(False, 'idle')

FLAG_OBJECT.set_sprites('emerge', k.resize_images(k.SIZE_FLAGS, (
    '../Images/flag_obj_emerge0.png',
    '../Images/flag_obj_emerge1.png',
    '../Images/flag_obj_emerge2.png',
    '../Images/flag_obj_emerge3.png',
    '../Images/flag_obj_emerge4.png',
    '../Images/flag_obj_emerge5.png',
    '../Images/flag_obj_emerge5.png',
)))

FLAG_OBJECT.set_sprites('idle', k.resize_images(k.SIZE_FLAGS, (
    '../Images/flag_obj_idle0.png',
    '../Images/flag_obj_idle1.png',
    '../Images/flag_obj_idle2.png',
)))

# COLETÁVEL DE VIDA
LIFE_COLLECTABLE = Sprites.LifeCollectable(MIAUSMA, False, 'idle', k.LIFETIME_COLLECTABLES)

LIFE_COLLECTABLE.set_sprites('emerge', k.resize_images(k.SIZE_COLLECTABLES, (
    '../Images/life_cll_emerge0.png',
    '../Images/life_cll_emerge1.png',
    '../Images/life_cll_emerge2.png',
    '../Images/life_cll_emerge3.png',
    '../Images/life_cll_emerge4.png',
    '../Images/life_cll_emerge5.png',
    '../Images/life_cll_emerge5.png',
)))

LIFE_COLLECTABLE.set_sprites('idle', k.resize_images(k.SIZE_COLLECTABLES, (
    '../Images/life_cll_idle0.png',
    '../Images/life_cll_idle1.png',
    '../Images/life_cll_idle2.png',
    '../Images/life_cll_idle3.png',
    '../Images/life_cll_idle4.png',
    '../Images/life_cll_idle5.png',
)))

# COLETÁVEL DE TEMPO
TIME_COLLECTABLE = Sprites.TimeCollectable(MIAUSMA, False, 'idle', k.LIFETIME_COLLECTABLES)

TIME_COLLECTABLE.set_sprites('emerge', k.resize_images(k.SIZE_COLLECTABLES, (
    '../Images/time_cll_emerge0.png',
    '../Images/time_cll_emerge1.png',
    '../Images/time_cll_emerge2.png',
    '../Images/time_cll_emerge3.png',
    '../Images/time_cll_emerge4.png',
    '../Images/time_cll_emerge5.png',
    '../Images/time_cll_emerge5.png',
)))

TIME_COLLECTABLE.set_sprites('idle', k.resize_images(k.SIZE_COLLECTABLES, (
    '../Images/time_cll_idle0.png',
    '../Images/time_cll_idle1.png',
    '../Images/time_cll_idle2.png',
    '../Images/time_cll_idle3.png',
    '../Images/time_cll_idle4.png',
    '../Images/time_cll_idle5.png',
)))

# COLETÁVEL DE BANDEIRA (NÃO IMPLEMENTADO)
'''FLAG_COLLECTABLE = Sprites.FlagCollectable(MIAUSMA, False, 'idle', k.LIFETIME_COLLECTABLES)

FLAG_COLLECTABLE.set_sprites('emerge', k.resize_images(k.SIZE_COLLECTABLES, (
    '../Images/flag_cll_emerge0.png',
    '../Images/flag_cll_emerge1.png',
    '../Images/flag_cll_emerge2.png',
    '../Images/flag_cll_emerge3.png',
    '../Images/flag_cll_emerge4.png',
    '../Images/flag_cll_emerge5.png',
    '../Images/flag_cll_emerge5.png',
)))

FLAG_COLLECTABLE.set_sprites('idle', k.resize_images(k.SIZE_COLLECTABLES, (
    '../Images/flag_cll_idle0.png',
    '../Images/flag_cll_idle1.png',
    '../Images/flag_cll_idle2.png',
    '../Images/flag_cll_idle3.png',
    '../Images/flag_cll_idle4.png',
    '../Images/flag_cll_idle5.png',
)))'''

# INICIALIZANDO ANIMAÇÃO DOS OBJETOS E COLETÁVEIS
FLAG_OBJECT.set_animation('emerge', (-1000, -1000), 7)
LIFE_COLLECTABLE.set_animation('emerge', (-1000, -1000), 7)
TIME_COLLECTABLE.set_animation('emerge', (-1000, -1000), 7)

# GRUPO DE SPRITES DO JOGO
PURGATORY = pygame.sprite.LayeredUpdates()
PURGATORY.add(MIAUSMA)
PURGATORY.add(LIFE_COLLECTABLE)
PURGATORY.add(TIME_COLLECTABLE)

# PLANO DE FUNDO DO MENU PRINCIPAL
BACKGROUND_MAIN_MENU = k.resize_image(k.SCREEN_DIMENSIONS, '../Images/background_main_menu.png')

# BOTÕES
TO_MAIN_GAME_BUTTON = Interfaces.ToMainGameButton(k.TO_MAIN_GAME_BUTTON_SIZE, k.TO_MAIN_GAME_BUTTON_POSITION, MOUSE, None)
QUIT_GAME_BUTTON = Interfaces.QuitGameButton(k.QUIT_GAME_BUTTON_SIZE, k.QUIT_GAME_BUTTON_POSITION, MOUSE)

# PARTE LÓGICA DO CAMPO MINADO
ABSTRACT_MINEFIELD = Algoritmos.AbstractMinefield(k.ABSTRACT_MINEFIELD_SIZE, k.ABSTRACT_MINEFIELD_DENSITY)

# PARTE INTERAGÍVEL DO CAMPO MINADO
MINEFIELD = Interfaces.TileGrid(k.MINEFIELD_SIZE, k.MINEFIELD_POSITION, MOUSE, Interfaces.Tile, (k.MINEFIELD_SIZE[0] // k.ABSTRACT_MINEFIELD_SIZE[0], k.MINEFIELD_SIZE[1] // k.ABSTRACT_MINEFIELD_SIZE[1]), ABSTRACT_MINEFIELD)

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
        current_state = self.gsm.get_state()

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

                # LIMPOU O CAMPO MINADO
                if event.type == k.MINESWEEPER_WIN:
                    # PREENCHE O CAMPO MINADO MAIS UMA VEZ
                    ABSTRACT_MINEFIELD.__init__(k.ABSTRACT_MINEFIELD_SIZE, k.ABSTRACT_MINEFIELD_DENSITY)
                    MINEFIELD.__init__(k.MINEFIELD_SIZE, k.MINEFIELD_POSITION, MOUSE, Interfaces.Tile, (k.MINEFIELD_SIZE[0] // k.ABSTRACT_MINEFIELD_SIZE[0], k.MINEFIELD_SIZE[1] // k.ABSTRACT_MINEFIELD_SIZE[1]), ABSTRACT_MINEFIELD)
                    MINEFIELD.fill_matrix()

                    # ELIMINA TODOS OS SPRITES QUE NÃO SÃO O PROTAGONISTA
                    for sprite in PURGATORY:
                        if sprite != MIAUSMA:
                            sprite.kill()
                    Sprites.Flag.placed_flags.clear()

                    # ESCAVA O LADRILHO ONDE ESTÁ O PROTAGONISTA AUTOMATICAMENTE
                    dig_tile = MINEFIELD.get_tile(MIAUSMA.rect.center)
                    dig_tile.minefield.dig(dig_tile.coordinates)

                # DESCOBRIU UM LADRILHO LIVRE NO CAMPO MINADO (IGNORA REAÇÕES EM CADEIA)
                if event.type == k.MINESWEEPER_PRIMARY_HIT:
                    tile_x, tile_y = event.coordinates
                    hit_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    MIAUSMA.rect.center = hit_tile.rect.center
                    MIAUSMA.set_current_speed([0, 0])
                    MIAUSMA.set_animation('dig', MIAUSMA.get_position(), 7)
                    MIAUSMA.digging = True

                # DESCOBRIU UM LADRILHO LIVRE NO CAMPO MINADO
                if event.type == k.MINESWEEPER_HIT:
                    tile_x, tile_y = event.coordinates
                    generation_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    tile_x, tile_y = generation_tile.rect.topleft
                    tile_x_size, tile_y_size = generation_tile.get_size()
                    life_x_size, life_y_size = LIFE_COLLECTABLE.rect.size

                    # GERAÇÃO ALEATÓRIA DE COLETÁVEIS
                    if randint(1, k.RNG_LIFE_COLLECTABLE) == 1:
                        LIFE_COLLECTABLE.generate((tile_x + tile_x_size * 0.5 - life_x_size * 0.5, tile_y + tile_y_size * 0.5 - life_y_size * 0.5), PURGATORY, 1)
                    if randint(1, k.RNG_TIME_COLLECTABLE) == 1:
                        TIME_COLLECTABLE.generate((tile_x + tile_x_size * 0.5 - life_x_size * 0.5, tile_y + tile_y_size * 0.5 - life_y_size * 0.5), PURGATORY, 1)

                # ACERTOU UMA BOMBA NO CAMPO MINADO
                if event.type == k.MINESWEEPER_MISS:
                    MIAUSMA.damage(1)

                # PLANTOU UMA BANDEIRA NO CAMPO MINADO
                if event.type == k.MINESWEEPER_FLAG:
                    tile_x, tile_y = event.coordinates
                    generation_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    tile_x, tile_y = generation_tile.rect.topleft
                    tile_x_size, tile_y_size = generation_tile.get_size()
                    flag_x_size, flag_y_size = FLAG_OBJECT.rect.size

                    # GERA A BANDEIRA
                    placed_flags = Sprites.Flag.placed_flags
                    new_flag = FLAG_OBJECT.generate((tile_x, tile_y - tile_y_size), PURGATORY, 1)
                    placed_flags[event.coordinates] = new_flag

                    # REMOVE SPRITES DE BANDEIRA EM EXCESSO PARA CONSERVAR PERFORMANCE
                    if len(placed_flags) > k.FLAG_LIMIT:
                        remove_flag = placed_flags.pop(next(iter(placed_flags)))
                        remove_flag.kill()

                # REMOVEU UMA BANDEIRA DO CAMPO MINADO
                if event.type == k.MINESWEEPER_UNFLAG:
                    placed_flags = Sprites.Flag.placed_flags
                    if event.coordinates in placed_flags:
                        placed_flags[event.coordinates].kill()
                        del placed_flags[event.coordinates]

                # OBJETO DO TIMER CHEGOU A ZERO
                if event.type == k.RING_EVENT:
                    pass

            # MOVIMENTAÇÃO E EFEITOS DE PROXIMIDADE NO JOGO
            if current_state == MainGame:
                move_keys = pygame.key.get_pressed()

                move_left = move_keys[pygame.K_a] or move_keys[pygame.K_LEFT]
                move_right = move_keys[pygame.K_d] or move_keys[pygame.K_RIGHT]
                move_up = move_keys[pygame.K_w] or move_keys[pygame.K_UP]
                move_down = move_keys[pygame.K_s] or move_keys[pygame.K_DOWN]

                move_up_left = move_up and move_left
                move_up_right = move_up and move_right
                move_down_left = move_down and move_left
                move_down_right = move_down and move_right

                if move_up_left:
                    MIAUSMA.face(6)
                elif move_up_right:
                    MIAUSMA.face(7)
                elif move_down_left:
                    MIAUSMA.face(5)
                elif move_down_right:
                    MIAUSMA.face(8)
                elif move_left:
                    MIAUSMA.face(2)
                elif move_right:
                    MIAUSMA.face(4)
                elif move_up:
                    MIAUSMA.face(3)
                elif move_down:
                    MIAUSMA.face(1)
                else:
                    MIAUSMA.face(0)

                minefield_x_size, minefield_y_size = k.MINEFIELD_SIZE
                minefield_x, minefield_y = k.MINEFIELD_POSITION
                miausma_x_size, miausma_y_size = k.MIAUSMA_SIZE
                miausma_x, miausma_y = MIAUSMA.get_position()
                miausma_x_speed, miausma_y_speed = MIAUSMA.get_current_speed()

                if miausma_x < minefield_x:
                    MIAUSMA.set_position((minefield_x, miausma_y))
                    MIAUSMA.set_current_speed([0, miausma_y_speed])
                if miausma_x + miausma_x_size > minefield_x + minefield_x_size:
                    MIAUSMA.set_position((minefield_x + minefield_x_size - miausma_x_size, miausma_y))
                    MIAUSMA.set_current_speed([0, miausma_y_speed])
                if miausma_y < minefield_y:
                    MIAUSMA.set_position((miausma_x, minefield_y))
                    MIAUSMA.set_current_speed([miausma_x_speed, 0])
                if miausma_y + miausma_y_size > minefield_y + minefield_y_size:
                    MIAUSMA.set_position((miausma_x, minefield_y + minefield_y_size - miausma_y_size))
                    MIAUSMA.set_current_speed([miausma_x_speed, 0])

                MIAUSMA.move((move_left, move_right, move_up, move_down))

                if MOUSE.position and minefield_x + minefield_x_size > MOUSE.position[0] > minefield_x:
                    tile_x, tile_y = MINEFIELD.get_tile(MOUSE.position).coordinates
                    miausma_x, miausma_y = MINEFIELD.get_minefield_coordinates(MIAUSMA.rect.center)
                    if (abs(tile_x - miausma_x), abs(tile_y - miausma_y)) <= (2, 2):
                        mouse_x, mouse_y = MOUSE.position
                        MINEFIELD.get_tile((mouse_x, mouse_y)).close_to_player = True

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
        # INSERE O PLANO DE FUNDO NA TELA
        self.screen.put_inside(BACKGROUND_MAIN_MENU, (0, 0))

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

        # INSERE OS SPRITES DO JOGO NA TELA
        PURGATORY.draw(self.screen.display)

        # CARREGA O CAMPO MINADO NA TELA
        MINEFIELD.update()

        # CARREGA OS SPRITES DO JOGO NA TELA
        PURGATORY.update()
