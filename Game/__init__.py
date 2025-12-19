import pygame
import Interfaces
import Sounds
import Sprites
import Others
import Constantes as k
import Algoritmos

from random import randint, choice

# PRÉ-INICIALIZANDO O MIXER (OTIMIZAÇÃO)
pygame.mixer.pre_init(44100, 16, 2, 4096)

# INICIALIZANDO PYGAME
pygame.init()

# INICIALIZANDO DISPLAY
SCREEN = Interfaces.Screen()
SCREEN.set_title(k.GAME_TITLE)
SCREEN.set_size(k.SCREEN_DIMENSIONS)
SCREEN.show()

# PREPARANDO PLAYLISTS
PLAYLIST_MAIN_MENU = Sounds.Playlist(k.PLAYLIST_MAIN_MENU_MUSICS)
PLAYLIST_MAIN_MENU.queue_shuffle()
PLAYLIST_MAIN_MENU.set_volume(k.VOLUME_BGM)
PLAYLIST_MAIN_MENU.start()

PLAYLIST_MAIN_GAME = Sounds.Playlist(k.PLAYLIST_MAIN_GAME_MUSICS)
PLAYLIST_MAIN_GAME.queue_shuffle()

# PREPARANDO EFEITOS SONOROS
SFX_STORAGE = {
    'SELECT': Sounds.SFX('Audio/sfx/select.ogg', k.VOLUME_SFX),
    'OUCH': Sounds.SFX('Audio/sfx/ouch.ogg', k.VOLUME_SFX),
    'BLIP': Sounds.SFX('Audio/sfx/blip.ogg', k.VOLUME_SFX),
    'BOOM': Sounds.SFX('Audio/sfx/boom.ogg', k.VOLUME_SFX),
    'DIG': [Sounds.SFX('Audio/sfx/dig0.ogg', k.VOLUME_SFX), Sounds.SFX('Audio/sfx/dig1.ogg', k.VOLUME_SFX), Sounds.SFX('Audio/sfx/dig2.ogg', k.VOLUME_SFX)],
    'FLAG': Sounds.SFX('Audio/sfx/flag.ogg', k.VOLUME_SFX),
    'VICTORY': Sounds.SFX('Audio/sfx/victory.ogg', k.VOLUME_SFX),
    'MEOW': [Sounds.SFX('Audio/sfx/meow.ogg', k.VOLUME_SFX)],
    'LOAD': Sounds.SFX('Audio/sfx/load.ogg', k.VOLUME_SFX),
    'SHOOT': Sounds.SFX('Audio/sfx/shoot.ogg', k.VOLUME_SFX),
    'CHEER': Sounds.SFX('Audio/sfx/cheer.ogg', k.VOLUME_SFX),
    'SCREAM': Sounds.SFX('Audio/sfx/scream.ogg', k.VOLUME_SFX),
}

# OBJETO DO MOUSE
MOUSE = Others.Mouse()

# FONTE CUSTOMIZADA
PURGE_SERIF_175 = pygame.font.Font('Fonts/purge_serif.ttf', 175)
PURGE_SERIF_180 = pygame.font.Font('Fonts/purge_serif.ttf', 180)
PURGE_SERIF_415 = pygame.font.Font('Fonts/purge_serif.ttf', 415)

# FONTE EXTRA
FUZZY_BUBBLES_40 = pygame.font.Font('Fonts/fuzzy_bubbles.ttf', 40)
FUZZY_BUBBLES_60 = pygame.font.Font('Fonts/fuzzy_bubbles.ttf', 60)
FUZZY_BUBBLES_100 = pygame.font.Font('Fonts/fuzzy_bubbles.ttf', 80)

# PLANO DE FUNDO DO MENU PRINCIPAL
BACKGROUND_MAIN_MENU = k.resize_image(k.SCREEN_DIMENSIONS, 'Images/background_main_menu.png')
BACKGROUND_MAIN_GAME = k.resize_image(k.SCREEN_DIMENSIONS, 'Images/background_main_game.png')

BACKGROUND_MAIN_MENU_DRAWN = []
BACKGROUND_MAIN_GAME_DRAWN = []

# PROTAGONISTA
MIAUSMA = Sprites.Player(k.MIAUSMA_MAX_SPEED, k.MIAUSMA_ACC, k.MIAUSMA_DAMPEN, k.MIAUSMA_CDAMP)

MIAUSMA.set_sprites('idle', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/idle0.png',
    'Images/idle1.png',
    'Images/idle2.png',
    'Images/idle3.png',
    'Images/idle4.png',
    'Images/idle5.png',
)))

MIAUSMA.set_sprites('walk up', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_up0.png',
    'Images/walk_up1.png',
    'Images/walk_up2.png',
    'Images/walk_up3.png',
    'Images/walk_up4.png',
    'Images/walk_up5.png'
)))

MIAUSMA.set_sprites('walk down', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_down0.png',
    'Images/walk_down1.png',
    'Images/walk_down2.png',
    'Images/walk_down3.png',
    'Images/walk_down4.png',
    'Images/walk_down5.png'
)))

MIAUSMA.set_sprites('walk left', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_left0.png',
    'Images/walk_left1.png',
    'Images/walk_left2.png',
    'Images/walk_left3.png',
    'Images/walk_left4.png',
    'Images/walk_left5.png'
)))

MIAUSMA.set_sprites('walk right', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_right0.png',
    'Images/walk_right1.png',
    'Images/walk_right2.png',
    'Images/walk_right3.png',
    'Images/walk_right4.png',
    'Images/walk_right5.png'
)))

MIAUSMA.set_sprites('walk down left', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_down_left0.png',
    'Images/walk_down_left1.png',
    'Images/walk_down_left2.png',
    'Images/walk_down_left3.png',
    'Images/walk_down_left4.png',
    'Images/walk_down_left5.png'
)))

MIAUSMA.set_sprites('walk up left', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_up_left0.png',
    'Images/walk_up_left1.png',
    'Images/walk_up_left2.png',
    'Images/walk_up_left3.png',
    'Images/walk_up_left4.png',
    'Images/walk_up_left5.png'
)))

MIAUSMA.set_sprites('walk up right', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_up_right0.png',
    'Images/walk_up_right1.png',
    'Images/walk_up_right2.png',
    'Images/walk_up_right3.png',
    'Images/walk_up_right4.png',
    'Images/walk_up_right5.png'
)))

MIAUSMA.set_sprites('walk down right', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/walk_down_right0.png',
    'Images/walk_down_right1.png',
    'Images/walk_down_right2.png',
    'Images/walk_down_right3.png',
    'Images/walk_down_right4.png',
    'Images/walk_down_right5.png'
)))

MIAUSMA.set_sprites('dig', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/dig0.png',
    'Images/dig1.png',
    'Images/dig2.png',
    'Images/dig3.png',
    'Images/dig4.png',
    'Images/dig5.png'
)))

MIAUSMA.set_sprites('hurt', k.resize_images(k.MIAUSMA_SIZE, (
    'Images/hurt0.png',
    'Images/hurt1.png',
    'Images/hurt2.png',
    'Images/hurt3.png',
    'Images/hurt4.png',
    'Images/hurt5.png'
)))

MIAUSMA.bind_facing_sprites(('idle', 'walk down', 'walk left', 'walk up', 'walk right', 'walk down left', 'walk up left', 'walk up right', 'walk down right'))
MIAUSMA.set_animation('idle', k.set_proportion(2.14, 2.24), 7)

MIAUSMA_REACTS = Sprites.Sprite()

# REAÇÃO BASE QUE MUDA QUANDO O TEMPO ESTÁ ACABANDO
MIAUSMA_REACTS_BASE = ['normal']

MIAUSMA_REACTS.set_sprites('normal', k.resize_images(k.MIAUSMA_REACT_SIZE, (
    'Images/REAGE_NORMAL0.png',
    'Images/REAGE_NORMAL1.png',
    'Images/REAGE_NORMAL2.png',
    'Images/REAGE_NORMAL3.png',
    'Images/REAGE_NORMAL4.png',
    'Images/REAGE_NORMAL5.png'
)))

MIAUSMA_REACTS.set_sprites('sem tempo', k.resize_images(k.MIAUSMA_REACT_SIZE, (
    'Images/REAGE_SEM_TEMPO0.png',
    'Images/REAGE_SEM_TEMPO1.png',
    'Images/REAGE_SEM_TEMPO2.png',
    'Images/REAGE_SEM_TEMPO3.png',
    'Images/REAGE_SEM_TEMPO4.png',
    'Images/REAGE_SEM_TEMPO5.png'
)))

MIAUSMA_REACTS.set_sprites('chora', k.resize_images(k.MIAUSMA_REACT_SIZE, (
    'Images/REAGE_CHORA0.png',
    'Images/REAGE_CHORA1.png',
    'Images/REAGE_CHORA2.png',
    'Images/REAGE_CHORA3.png',
    'Images/REAGE_CHORA4.png',
    'Images/REAGE_CHORA5.png'
)))

MIAUSMA_REACTS.set_sprites('choque', k.resize_images(k.MIAUSMA_REACT_SIZE, (
    'Images/REAGE_CHOQUE0.png',
    'Images/REAGE_CHOQUE1.png',
    'Images/REAGE_CHOQUE2.png',
    'Images/REAGE_CHOQUE3.png',
    'Images/REAGE_CHOQUE4.png',
    'Images/REAGE_CHOQUE5.png'
)))

# INICIALIZANDO REAÇÕES DO PROTAGONISTA
MIAUSMA_REACTS.set_animation('normal', k.MIAUSMA_REACT_POSITION, 3)

# BANDEIRAS
FLAG_OBJECT = Sprites.Flag(False, 'idle')

FLAG_OBJECT.set_sprites('emerge', k.resize_images(k.SIZE_FLAGS, (
    'Images/flag_obj_emerge0.png',
    'Images/flag_obj_emerge1.png',
    'Images/flag_obj_emerge2.png',
    'Images/flag_obj_emerge3.png',
    'Images/flag_obj_emerge4.png',
    'Images/flag_obj_emerge5.png',
    'Images/flag_obj_emerge5.png',
)))

FLAG_OBJECT.set_sprites('idle', k.resize_images(k.SIZE_FLAGS, (
    'Images/flag_obj_idle0.png',
    'Images/flag_obj_idle1.png',
    'Images/flag_obj_idle2.png',
)))

# BOMBAS
BOMB_OBJECT = Sprites.Bomb(False, 'charge', 'explode')

BOMB_OBJECT.set_sprites('emerge', k.resize_images(k.SIZE_BOMBS, (
    'Images/bomb_obj_emerge0.png',
    'Images/bomb_obj_emerge1.png',
    'Images/bomb_obj_emerge2.png',
    'Images/bomb_obj_emerge3.png',
    'Images/bomb_obj_emerge4.png',
    'Images/bomb_obj_emerge5.png',
    'Images/bomb_obj_emerge5.png',
)))

BOMB_OBJECT.set_sprites('charge', k.resize_images(k.SIZE_BOMBS, (
    'Images/bomb_obj_charge0.png',
    'Images/bomb_obj_charge1.png',
    'Images/bomb_obj_charge2.png',
    'Images/bomb_obj_charge3.png',
    'Images/bomb_obj_charge4.png',
    'Images/bomb_obj_charge5.png',
)))

BOMB_OBJECT.set_sprites('explode', k.resize_images(k.SIZE_BOMBS, (
    'Images/bomb_obj_explode0.png',
    'Images/bomb_obj_explode1.png',
    'Images/bomb_obj_explode2.png',
    'Images/bomb_obj_explode3.png',
    'Images/bomb_obj_explode4.png',
    'Images/bomb_obj_explode5.png',
)))

# COLETÁVEL DE VIDA
LIFE_COLLECTABLE = Sprites.LifeCollectable(MIAUSMA, False, 'idle', k.LIFETIME_COLLECTABLES)

LIFE_COLLECTABLE.set_sprites('emerge', k.resize_images(k.SIZE_COLLECTABLES, (
    'Images/life_cll_emerge0.png',
    'Images/life_cll_emerge1.png',
    'Images/life_cll_emerge2.png',
    'Images/life_cll_emerge3.png',
    'Images/life_cll_emerge4.png',
    'Images/life_cll_emerge5.png',
    'Images/life_cll_emerge5.png',
)))

LIFE_COLLECTABLE.set_sprites('idle', k.resize_images(k.SIZE_COLLECTABLES, (
    'Images/life_cll_idle0.png',
    'Images/life_cll_idle1.png',
    'Images/life_cll_idle2.png',
    'Images/life_cll_idle3.png',
    'Images/life_cll_idle4.png',
    'Images/life_cll_idle5.png',
)))

# COLETÁVEL DE TEMPO
TIME_COLLECTABLE = Sprites.TimeCollectable(MIAUSMA, False, 'idle', k.LIFETIME_COLLECTABLES)

TIME_COLLECTABLE.set_sprites('emerge', k.resize_images(k.SIZE_COLLECTABLES, (
    'Images/time_cll_emerge0.png',
    'Images/time_cll_emerge1.png',
    'Images/time_cll_emerge2.png',
    'Images/time_cll_emerge3.png',
    'Images/time_cll_emerge4.png',
    'Images/time_cll_emerge5.png',
    'Images/time_cll_emerge5.png',
)))

TIME_COLLECTABLE.set_sprites('idle', k.resize_images(k.SIZE_COLLECTABLES, (
    'Images/time_cll_idle0.png',
    'Images/time_cll_idle1.png',
    'Images/time_cll_idle2.png',
    'Images/time_cll_idle3.png',
    'Images/time_cll_idle4.png',
    'Images/time_cll_idle5.png',
)))

# COLETÁVEL DE BANDEIRA (NÃO IMPLEMENTADO)
FLAG_COLLECTABLE = Sprites.FlagCollectable(MIAUSMA, False, 'idle', k.LIFETIME_COLLECTABLES)

FLAG_COLLECTABLE.set_sprites('emerge', k.resize_images(k.SIZE_COLLECTABLES, (
    'Images/flag_cll_emerge0.png',
    'Images/flag_cll_emerge1.png',
    'Images/flag_cll_emerge2.png',
    'Images/flag_cll_emerge3.png',
    'Images/flag_cll_emerge4.png',
    'Images/flag_cll_emerge5.png',
    'Images/flag_cll_emerge5.png',
    'Images/flag_cll_emerge6.png',
)))

FLAG_COLLECTABLE.set_sprites('idle', k.resize_images(k.SIZE_COLLECTABLES, (
    'Images/flag_cll_idle0.png',
    'Images/flag_cll_idle1.png',
    'Images/flag_cll_idle2.png',
    'Images/flag_cll_idle3.png',
    'Images/flag_cll_idle4.png',
    'Images/flag_cll_idle5.png',
)))

# INICIALIZANDO ANIMAÇÃO DOS OBJETOS E COLETÁVEIS
FLAG_OBJECT.set_animation('emerge', (-1000, -1000), 7)
BOMB_OBJECT.set_animation('emerge', (-1000, -1000), 5)
LIFE_COLLECTABLE.set_animation('emerge', (-1000, -1000), 7)
TIME_COLLECTABLE.set_animation('emerge', (-1000, -1000), 7)
FLAG_COLLECTABLE.set_animation('emerge', (-1000, -1000), 7)

# GRUPO DE SPRITES DO JOGO
PURGATORY = pygame.sprite.LayeredUpdates()
PURGATORY.add(MIAUSMA, layer=1)
PURGATORY.add(MIAUSMA_REACTS)
PURGATORY.add(LIFE_COLLECTABLE)
PURGATORY.add(TIME_COLLECTABLE)
PURGATORY.add(FLAG_COLLECTABLE)

# BOTÕES
TO_MAIN_GAME_BUTTON = Interfaces.ToMainGameButton(k.TO_MAIN_GAME_BUTTON_SIZE, k.TO_MAIN_GAME_BUTTON_POSITION, MOUSE, None)
QUIT_GAME_BUTTON = Interfaces.QuitGameButton(k.QUIT_GAME_BUTTON_SIZE, k.QUIT_GAME_BUTTON_POSITION, MOUSE)
PAUSE_BUTTON = Interfaces.PauseButton(k.PAUSE_BUTTON_SIZE, k.PAUSE_BUTTON_POSITION, MOUSE, FUZZY_BUBBLES_60.render('PAUSE', True, k.COLOR_WHITE))

# APARÊNCIA DOS BOTÕES
TO_MAIN_GAME_BUTTON_MASK = Sprites.ButtonMask(TO_MAIN_GAME_BUTTON, 'idle', 'hover')
QUIT_GAME_BUTTON_MASK = Sprites.ButtonMask(QUIT_GAME_BUTTON, 'idle', 'hover')

TO_MAIN_GAME_BUTTON_MASK.set_sprites('idle', k.resize_images(k.TO_MAIN_GAME_BUTTON_MASK_SIZE, (
    'Images/to_main_game_btn_idle0.png',
    'Images/to_main_game_btn_idle1.png',
    'Images/to_main_game_btn_idle2.png',
    'Images/to_main_game_btn_idle3.png',
    'Images/to_main_game_btn_idle4.png',
    'Images/to_main_game_btn_idle5.png',
)))

TO_MAIN_GAME_BUTTON_MASK.set_sprites('hover', k.resize_images(k.TO_MAIN_GAME_BUTTON_MASK_SIZE, (
    'Images/to_main_game_btn_hover0.png',
    'Images/to_main_game_btn_hover1.png',
    'Images/to_main_game_btn_hover2.png',
    'Images/to_main_game_btn_hover3.png',
    'Images/to_main_game_btn_hover4.png',
    'Images/to_main_game_btn_hover5.png',
)))

QUIT_GAME_BUTTON_MASK.set_sprites('idle', k.resize_images(k.QUIT_GAME_BUTTON_MASK_SIZE, (
    'Images/quit_game_btn_idle0.png',
    'Images/quit_game_btn_idle1.png',
    'Images/quit_game_btn_idle2.png',
    'Images/quit_game_btn_idle3.png',
    'Images/quit_game_btn_idle4.png',
    'Images/quit_game_btn_idle5.png',
)))

QUIT_GAME_BUTTON_MASK.set_sprites('hover', k.resize_images(k.QUIT_GAME_BUTTON_MASK_SIZE, (
    'Images/quit_game_btn_hover0.png',
    'Images/quit_game_btn_hover1.png',
    'Images/quit_game_btn_hover2.png',
    'Images/quit_game_btn_hover3.png',
    'Images/quit_game_btn_hover4.png',
    'Images/quit_game_btn_hover5.png',
)))

TO_MAIN_GAME_BUTTON_MASK.set_animation('idle', TO_MAIN_GAME_BUTTON_MASK.button.rect.topleft, 3)
QUIT_GAME_BUTTON_MASK.set_animation('idle', QUIT_GAME_BUTTON_MASK.button.rect.topleft, 3)

BUTTON_MASKS = pygame.sprite.Group()
BUTTON_MASKS.add(TO_MAIN_GAME_BUTTON_MASK)
BUTTON_MASKS.add(QUIT_GAME_BUTTON_MASK)

# SUPERFÍCIES QUE SUBSTITUEM O BACKGROUND NO JOGO
LEFT_PLACEHOLDER = BACKGROUND_MAIN_GAME.subsurface((0, 0, k.MIAUSMA_REACT_SIZE[0], k.SCREEN_HEIGHT)).convert()
RIGHT_PLACEHOLDER = BACKGROUND_MAIN_GAME.subsurface((k.MIAUSMA_REACT_SIZE[0] + k.MINEFIELD_SIZE[0], 0, k.MIAUSMA_REACT_SIZE[0], k.SCREEN_HEIGHT)).convert()

# NOTA DO JOGADOR COM BASE NA PONTUAÇÃO
PLAYER_GRADE = [PURGE_SERIF_415.render('', True, k.COLOR_YELLOW)]

# TEXTO COM A PONTUAÇÃO
GAME_SCORE = [PURGE_SERIF_175.render(k.display_score(MIAUSMA.score), True, k.COLOR_WHITE)]

# TEXTO DE PONTUAÇÃO
GAME_SCORE_LABEL = FUZZY_BUBBLES_40.render('PONTUAÇÃO', True, k.COLOR_WHITE)

# TEXTO COM O MULTIPLICADOR
GAME_MULTIPLIER = [FUZZY_BUBBLES_60.render(k.display_multiplier(MIAUSMA.multiplier), True, k.COLOR_WHITE)]

# TEXTO DE TEMPO RESTANTE
TIME_LEFT_LABEL = FUZZY_BUBBLES_40.render('TEMPO RESTANTE', True, k.COLOR_WHITE)

# TEMPO RESTANTE
TIME_LEFT = [PURGE_SERIF_180.render(k.time_milliseconds_to_display(k.TIME_LIMIT_SECONDS * 1000), True, k.COLOR_WHITE)]

# TEXTO COM A CONTAGEM DE BANDEIRAS
FLAG_COUNTER = [FUZZY_BUBBLES_100.render(k.display_out_of(MIAUSMA.flags, MIAUSMA.max_flags), True, k.COLOR_WHITE)]

# IMAGEM DE BANDEIRA
FLAG_ICON = k.resize_image(k.FLAG_ICON_SIZE, 'Images/flag_cll_idle0.png')

# PLACAR DE VIDA E AS VIDAS
LIFE_DISPLAY = k.resize_image(k.LIFE_DISPLAY_SIZE, 'Images/placar_vidas.png')
SEVEN_LIVES = Interfaces.LifeIconArray(
    7, [k.resize_image(k.LIFE_ICON_SIZE, 'Images/heart_full.png') for _ in range(7)],
    k.resize_image(k.LIFE_ICON_SIZE, 'Images/heart_full.png'), k.resize_image(k.LIFE_ICON_SIZE, 'Images/heart_hollow.png')
)

# PARTE LÓGICA DO CAMPO MINADO
ABSTRACT_MINEFIELD = Algoritmos.AbstractMinefield(k.ABSTRACT_MINEFIELD_SIZE, k.ABSTRACT_MINEFIELD_DENSITY)

# PARTE INTERAGÍVEL DO CAMPO MINADO
MINEFIELD = Interfaces.TileGrid(k.MINEFIELD_SIZE, k.MINEFIELD_POSITION, MOUSE, Interfaces.Tile, (k.MINEFIELD_SIZE[0] // k.ABSTRACT_MINEFIELD_SIZE[0], k.MINEFIELD_SIZE[1] // k.ABSTRACT_MINEFIELD_SIZE[1]), ABSTRACT_MINEFIELD)

# PREENCHENDO CAMPO MINADO
MINEFIELD.fill_matrix()

# COMEÇO DO JOGO
GAME_START_VALUE = [None]

# DIÁLOGO DE PAUSE
PAUSE_DIALOGUE = FUZZY_BUBBLES_60.render('PRESSIONE ESC PARA RETORNAR AO JOGO', True, k.COLOR_WHITE)

# TIMER DO JOGO
GAME_TIMER = Others.Timer()

# TIMER DE DISPONIBILIDADE DOS LADRILHOS
AVAILABLE_TILE_TIMER = Others.Timer()

# TIMERS DEPOIS DO FIM
END_TIMERS = [Others.Timer() for _ in range(5)]

# TEXTO DA HORA DO JULGAMENTO
JUDGEMENT_TIME_LABEL = RETURN_DIALOGUE = FUZZY_BUBBLES_100.render('HORA DO JULGAMENTO', True, k.COLOR_WHITE)

# TEXTO DO JULGAMENTO
JUDGEMENT_LABEL = RETURN_DIALOGUE = FUZZY_BUBBLES_100.render('VOCÊ É...', True, k.COLOR_WHITE)

# PONTUAÇÃO FINAL
FINAL_SCORE = []

# DIÁLOGO DE RETORNO
RETURN_DIALOGUE = FUZZY_BUBBLES_40.render('PRESSIONE ESC PARA RETORNAR AO MENU PRINCIPAL', True, k.COLOR_WHITE)

# PONTUAÇÃO PARA CONTAR NA TELA FINAL
COUNTING_SCORE = [0]

class Game:

    def __init__(self, game_title, screen_size, fps):
        # CLOCK E TAXA DE QUADROS
        self.clock = pygame.time.Clock()
        self.FPS = fps

        # INFORMAÇÕES PARA A TELA INICIAL
        self.game_title = game_title
        self.screen_size = screen_size
        self.screen = None

        # GERENCIADOR DE ESTADOS
        self.gsm = None

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

            if self.gsm.get_state == EndScreen:
                self.gsm.run()
                SCREEN.update()
                continue

            # LOOP DE EVENTOS
            for event in pygame.event.get():

                # SAIR
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == k.GAME_PAUSE and not GAME_START_VALUE:
                    pause_start_time = pygame.time.get_ticks()
                    pygame.mixer.music.pause()
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                pause = False

                        if not pause:
                            pause_end_time = pygame.time.get_ticks()
                            GAME_TIMER.add_time_seconds((pause_end_time - pause_start_time) // 1000)
                            pygame.mixer.music.unpause()
                            break

                        SCREEN.fill(k.COLOR_BLACK)
                        SCREEN.put_inside(PAUSE_DIALOGUE, k.PAUSE_DIALOGUE_POSITION)
                        SCREEN.update()

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

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_e:
                        choice(SFX_STORAGE['MEOW']).play()

                # LIMPOU O CAMPO MINADO
                if event.type == k.MINESWEEPER_WIN:
                    SFX_STORAGE['VICTORY'].play()
                    MIAUSMA.score_points(1000 + MIAUSMA.lives * 100 + GAME_TIMER.get_current_time_seconds() * 100)
                    for tile_line in MINEFIELD.button_matrix:
                        for tile in tile_line:
                            if tile.code == 11:
                                MIAUSMA.score_points(20)

                    MIAUSMA.increment_multiplier()
                    GAME_MULTIPLIER[0] = FUZZY_BUBBLES_60.render(k.display_multiplier(MIAUSMA.multiplier), True, k.COLOR_WHITE)

                    # PREENCHE O CAMPO MINADO MAIS UMA VEZ
                    ABSTRACT_MINEFIELD.__init__(k.ABSTRACT_MINEFIELD_SIZE, k.ABSTRACT_MINEFIELD_DENSITY)
                    MINEFIELD.__init__(k.MINEFIELD_SIZE, k.MINEFIELD_POSITION, MOUSE, Interfaces.Tile, (k.MINEFIELD_SIZE[0] // k.ABSTRACT_MINEFIELD_SIZE[0], k.MINEFIELD_SIZE[1] // k.ABSTRACT_MINEFIELD_SIZE[1]), ABSTRACT_MINEFIELD)
                    MINEFIELD.fill_matrix()

                    # ELIMINA TODOS OS SPRITES QUE NÃO SÃO O PROTAGONISTA OU COLETÁVEIS
                    for sprite in PURGATORY:
                        if sprite != MIAUSMA and sprite != MIAUSMA_REACTS and not issubclass(sprite.__class__, (Sprites.Collectable, Sprites.Bomb)):
                            sprite.kill()
                    Sprites.Flag.placed_flags.clear()

                    # ESCAVA O LADRILHO ONDE ESTÁ O PROTAGONISTA AUTOMATICAMENTE
                    dig_tile = MINEFIELD.get_tile_absolute(MIAUSMA.rect.center)
                    dig_tile.minefield.dig(dig_tile.coordinates)

                # DESCOBRIU UM LADRILHO LIVRE NO CAMPO MINADO (IGNORA REAÇÕES EM CADEIA)
                if event.type == k.MINESWEEPER_PRIMARY_HIT:
                    choice(SFX_STORAGE['DIG']).play()
                    MIAUSMA.score_points(15)
                    tile_x, tile_y = event.coordinates
                    hit_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    MIAUSMA.rect.center = hit_tile.rect.center
                    MIAUSMA.set_current_speed([0, 0])
                    MIAUSMA.set_animation('dig', MIAUSMA.get_position(), 5)
                    MIAUSMA.digging = True

                    if GAME_START_VALUE:
                        GAME_START_VALUE.clear()
                        post_event = pygame.event.Event(k.GAME_START)
                        pygame.event.post(post_event)

                # DESCOBRIU UM LADRILHO LIVRE NO CAMPO MINADO
                if event.type == k.MINESWEEPER_HIT:

                    # ELIMINA AS BANDEIRAS QUE ESTIVEREM EM CAMPOS VAZIOS
                    placed_flags = Sprites.Flag.placed_flags
                    if event.coordinates in placed_flags:
                        placed_flags[event.coordinates].kill()
                        del placed_flags[event.coordinates]

                    MIAUSMA.score_points(5)
                    tile_x, tile_y = event.coordinates
                    generation_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    tile_x, tile_y = generation_tile.rect.topleft
                    tile_x_size, tile_y_size = generation_tile.get_size()
                    life_x_size, life_y_size = LIFE_COLLECTABLE.rect.size

                    # GERAÇÃO ALEATÓRIA DE COLETÁVEIS
                    if randint(1, k.RNG_LIFE_COLLECTABLE) == 1:
                        LIFE_COLLECTABLE.generate((tile_x + tile_x_size * 0.5 - life_x_size * 0.5, tile_y + tile_y_size * 0.5 - life_y_size * 0.5), PURGATORY, 2)
                    if randint(1, k.RNG_TIME_COLLECTABLE) == 1:
                        TIME_COLLECTABLE.generate((tile_x + tile_x_size * 0.5 - life_x_size * 0.5, tile_y + tile_y_size * 0.5 - life_y_size * 0.5), PURGATORY, 2)
                    if randint(1, k.RNG_FLAG_COLLECTABLE) == 1:
                        FLAG_COLLECTABLE.generate((tile_x + tile_x_size * 0.5 - life_x_size * 0.5, tile_y + tile_y_size * 0.5 - life_y_size * 0.5), PURGATORY, 2)

                # ACERTOU UMA BOMBA NO CAMPO MINADO
                if event.type == k.MINESWEEPER_MISS:
                    tile_x, tile_y = event.coordinates
                    generation_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    tile_x, tile_y = generation_tile.rect.center
                    bomb_x_size, bomb_y_size = BOMB_OBJECT.rect.size

                    # GERA A BOMBA
                    BOMB_OBJECT.generate((tile_x - bomb_x_size // 2, tile_y - bomb_y_size // 1.3), PURGATORY, 0)

                # PLANTOU UMA BANDEIRA NO CAMPO MINADO
                if event.type == k.MINESWEEPER_FLAG:
                    SFX_STORAGE['FLAG'].play()
                    MIAUSMA_REACTS.set_animation(MIAUSMA_REACTS_BASE[0], k.MIAUSMA_REACT_POSITION, 3)
                    MIAUSMA.flag_down(1)
                    if not GAME_START_VALUE:
                        MIAUSMA.score_points(5)

                    if MIAUSMA.flags <= 0:
                        MINEFIELD.set_flag_unavailable()

                    tile_x, tile_y = event.coordinates
                    generation_tile = MINEFIELD.button_matrix[tile_x][tile_y]
                    tile_x, tile_y = generation_tile.rect.topleft
                    tile_x_size, tile_y_size = generation_tile.get_size()

                    # GERA A BANDEIRA
                    placed_flags = Sprites.Flag.placed_flags
                    new_flag = FLAG_OBJECT.generate((tile_x, tile_y - tile_y_size), PURGATORY, 0)
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

                # O PROTAGONISTA SOFREU DANO
                if event.type == k.DAMAGE_PLAYER:
                    SFX_STORAGE['BOOM'].play()
                    if randint(1, 2) == 1:
                        MIAUSMA_REACTS.set_animation('chora', k.MIAUSMA_REACT_POSITION, 3)
                    else:
                        MIAUSMA_REACTS.set_animation('choque', k.MIAUSMA_REACT_POSITION, 1)
                    MINEFIELD.set_damage_unavailable()
                    AVAILABLE_TILE_TIMER.set_timer_seconds(1)
                    AVAILABLE_TILE_TIMER.activate()
                    MIAUSMA.set_mode('hurt')
                    MIAUSMA.damage(1)
                    SEVEN_LIVES.set_lives(MIAUSMA.lives)

                # ENTROU-SE NA TELA DO JOGO
                if event.type == k.TO_MAIN_GAME_TRANSITION:
                    SFX_STORAGE['SELECT'].play()
                    PLAYLIST_MAIN_MENU.stop(1)

                # O CURSOR COMEÇA A PAIRAR SOBRE UM BOTÃO
                if event.type == k.BUTTON_HOVER:
                    SFX_STORAGE['BLIP'].play()

                # JOGADOR COLETOU UM COLETÁVEL
                if event.type == k.GET_COLLECTABLE:
                    MIAUSMA_REACTS.set_animation(MIAUSMA_REACTS_BASE[0], k.MIAUSMA_REACT_POSITION, 3)

                    if event.caller.__class__ == Sprites.LifeCollectable:
                        MIAUSMA.heal(1)
                        SEVEN_LIVES.set_lives(MIAUSMA.lives)

                    if event.caller.__class__ == Sprites.TimeCollectable:
                        GAME_TIMER.add_time_seconds(3)

                    if event.caller.__class__ == Sprites.FlagCollectable:
                        MINEFIELD.set_flag_available()
                        MIAUSMA.flag_up(1)

                # PROTAGONISTA SE CUROU ALÉM DO NECESSÁRIO
                if event.type == k.OVERHEAL:
                    MIAUSMA.score_points(200)

                # PROTAGONISTA PEGOU MAIS BANDEIRAS QUE O NECESSÁRIO
                if event.type == k.OVERFLAG:
                    MIAUSMA.score_points(100)

                # O JOGO COMEÇOU
                if event.type == k.GAME_START:
                    PLAYLIST_MAIN_GAME.start()
                    GAME_TIMER.set_timer_seconds(k.TIME_LIMIT_SECONDS)
                    GAME_TIMER.activate()

                # O JOGO ACABOU
                if event.type == k.GAME_OVER:
                    MIAUSMA_REACTS.set_animation('chora', k.MIAUSMA_REACT_POSITION, 3)
                    MINEFIELD.set_damage_unavailable()
                    GAME_START_VALUE.append(None)
                    PLAYLIST_MAIN_GAME.stop(1)
                    PLAYLIST_MAIN_GAME.next()
                    END_TIMERS[0].set_timer_seconds(3)
                    END_TIMERS[0].activate()
                    FINAL_SCORE.append(MIAUSMA.score)
                    GAME_SCORE[0] = PURGE_SERIF_175.render(k.display_score(0), True, k.COLOR_WHITE)
                    self.gsm.set_state('end screen')
                    break

            if self.gsm.get_state == EndScreen:
                continue

            # TEMPO ACABOU
            if GAME_TIMER.ring():
                TIME_LEFT[0] = PURGE_SERIF_180.render(k.time_milliseconds_to_display(0), True, k.COLOR_WHITE)
                post_event = pygame.event.Event(k.GAME_OVER)
                pygame.event.post(post_event)
            # TEMPO AINDA NÃO ACABOU
            elif GAME_TIMER.get_current_time_seconds():
                TIME_LEFT[0] = PURGE_SERIF_180.render(k.time_milliseconds_to_display(GAME_TIMER.current_time), True, k.COLOR_WHITE)

                if GAME_TIMER.get_current_time_seconds() < 20:
                    MIAUSMA_REACTS_BASE[0] = 'sem tempo'

            # PROTAGONISTA NÃO ESTÁ MAIS ATORDOADO
            if AVAILABLE_TILE_TIMER.ring() and not GAME_START_VALUE:
                SFX_STORAGE['OUCH'].play()
                MINEFIELD.set_damage_available()
                MIAUSMA.wake()

            if not GAME_START_VALUE:
                # RENDERIZAÇÃO DA NOTA E PONTUAÇÃO DO JOGADOR
                PLAYER_GRADE[0] = PURGE_SERIF_415.render(k.score_grade(MIAUSMA.score), True, k.COLOR_YELLOW)
                GAME_SCORE[0] = PURGE_SERIF_175.render(k.display_score(MIAUSMA.score), True, k.COLOR_WHITE)

            # RENDERIZAÇÃO DA QUANTIDADE DE BANDEIRAS DO JOGADOR
            FLAG_COUNTER[0] = FUZZY_BUBBLES_100.render(k.display_out_of(MIAUSMA.flags, MIAUSMA.max_flags), True, k.COLOR_WHITE)

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
                    miausma_x, miausma_y = MINEFIELD.get_minefield_coordinates(MIAUSMA.rect.center)

                    for tile_x in range(k.ABSTRACT_MINEFIELD_SIZE[0]):
                        for tile_y in range(k.ABSTRACT_MINEFIELD_SIZE[1]):
                            color_tile = MINEFIELD.get_tile_abstract((tile_x, tile_y))
                            if abs(tile_x - miausma_x) <= k.MIAUSMA_RANGE and abs(tile_y - miausma_y) <= k.MIAUSMA_RANGE:
                                color_tile.proximity_available = True
                                if MINEFIELD.minefield.minefield_interface[tile_x][tile_y] == 0 and not MIAUSMA.damaged:
                                    aura = pygame.surface.Surface(color_tile.get_size(), pygame.SRCALPHA)
                                    aura.fill(k.COLOR_ALPHA32_YELLOW)
                                    color_tile.blit(aura, (0, 0))
                            else:
                                color_tile.proximity_available = False

            # DECIDINDO QUAL TELA ESTÁ SENDO EXECUTADA
            current_state = self.gsm.get_state()
            current_state(SCREEN, self.gsm).run()

            # DESFAZ O CLIQUE INICIAL DO MOUSE
            MOUSE.reset_left_click()
            MOUSE.reset_right_click()

            # ATUALIZA O DISPLAY
            SCREEN.update()

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
        if not BACKGROUND_MAIN_MENU_DRAWN:
            # INSERE O PLANO DE FUNDO NA TELA
            BACKGROUND_MAIN_MENU_DRAWN.append(None)
            self.screen.put_inside(BACKGROUND_MAIN_MENU, (0, 0))

        # INSERE OS BOTÕES NA TELA
        self.screen.put_inside(TO_MAIN_GAME_BUTTON, TO_MAIN_GAME_BUTTON.rect.topleft)
        self.screen.put_inside(QUIT_GAME_BUTTON, QUIT_GAME_BUTTON.rect.topleft)

        BUTTON_MASKS.draw(self.screen.display)

        # CARREGA OS BOTÕES E A APARÊNCIA DELES NA TELA
        TO_MAIN_GAME_BUTTON.update()
        QUIT_GAME_BUTTON.update()
        BUTTON_MASKS.update()

class MainGame:

    def __init__(self, screen, gsm):
        # INICIA UMA RODADA DO JOGO
        self.screen = screen
        self.gsm = gsm

    def run(self):
        if not BACKGROUND_MAIN_GAME_DRAWN:
            # INSERE O PLANO DE FUNDO NA TELA
            BACKGROUND_MAIN_GAME_DRAWN.append(None)
            self.screen.put_inside(BACKGROUND_MAIN_GAME, (0, 0))

        # INSERE O CAMPO MINADO NA TELA
        self.screen.put_inside(MINEFIELD, MINEFIELD.rect.topleft)

        # INSERE OS PLACEHOLDERS PARA AS INTERFACES LATERAIS
        self.screen.put_inside(LEFT_PLACEHOLDER, (0, 0))
        self.screen.put_inside(RIGHT_PLACEHOLDER, (k.MIAUSMA_REACT_SIZE[0] + k.MINEFIELD_SIZE[0], 0))

        # INSERE A NOTA DO PLAYER NA TELA
        self.screen.put_inside(PLAYER_GRADE[0], k.PLAYER_GRADE_POSITION)

        # INSERE A PONTUAÇÃO NA TELA
        self.screen.put_inside(GAME_SCORE[0], k.GAME_SCORE_POSITION)

        # INSERE O TEXTO DE PONTUAÇÃO NA TELA
        self.screen.put_inside(GAME_SCORE_LABEL, k.GAME_SCORE_LABEL_POSITION)

        # INSERE O MULTIPLICADOR NA TELA
        self.screen.put_inside(GAME_MULTIPLIER[0], k.GAME_MULTIPLIER_POSITION)

        # INSERE O BOTÃO DE PAUSE NA TELA
        self.screen.put_inside(PAUSE_BUTTON, k.PAUSE_BUTTON_POSITION)

        # INSERE O TEXTO DE TEMPO RESTANTE NA TELA
        self.screen.put_inside(TIME_LEFT_LABEL, k.TIME_LEFT_LABEL_POSITION)

        # INSERE O TEMPO RESTANTE NA TELA
        self.screen.put_inside(TIME_LEFT[0], k.TIME_LEFT_POSITION)

        # INSERE O CONTADOR DE BANDEIRAS NA TELA
        self.screen.put_inside(FLAG_COUNTER[0], k.FLAG_COUNTER_POSITION)

        # INSERE O ÍCONE DE BANDEIRA NA TELA
        self.screen.put_inside(FLAG_ICON, k.FLAG_ICON_POSITION)

        # INSERE O PLACAR DE VIDA NA TELA
        self.screen.put_inside(LIFE_DISPLAY, k.LIFE_DISPLAY_POSITION)

        # ATUALIZA AS VIDAS NO PLACAR DE VIDA
        SEVEN_LIVES.update()

        # INSERE OS ÍCONES DE VIDA NA TELA
        for position, life in enumerate(SEVEN_LIVES.life_array):
            self.screen.put_inside(life, k.LIFE_ICONS_POSITION[position])

        # INSERE OS SPRITES DO JOGO NA TELA
        PURGATORY.draw(self.screen.display)

        # CARREGA O BOTÃO DE PAUSE NA TELA
        PAUSE_BUTTON.update()

        # CARREGA O CAMPO MINADO NA TELA
        MINEFIELD.update()

        # CARREGA OS SPRITES DO JOGO NA TELA
        PURGATORY.update()

class EndScreen:

    def __init__(self, screen, gsm):
        # INICIA A TELA DO FIM DE JOGO
        self.screen = screen
        self.gsm = gsm

    def run(self):
        if END_TIMERS[0].ring():
            self.screen.fill(k.COLOR_BLACK)
            END_TIMERS[1].set_timer_seconds(3)
            END_TIMERS[1].activate()
        elif END_TIMERS[0].activated:
            pygame.draw.line(self.screen.display, k.COLOR_BLACK, (randint(0, k.SCREEN_WIDTH), randint(0, k.SCREEN_HEIGHT)), (randint(0, k.SCREEN_WIDTH), randint(0, k.SCREEN_HEIGHT)), 100)

        if END_TIMERS[1].ring():
            self.screen.put_inside(JUDGEMENT_TIME_LABEL, k.JUDGEMENT_TIME_LABEL_POSITION)
            self.screen.put_inside(GAME_SCORE[0], k.GAME_SCORE_POSITION2)
            END_TIMERS[2].set_timer_seconds(3)
            END_TIMERS[2].activate()

        if END_TIMERS[2].ring():
            while COUNTING_SCORE[0] < FINAL_SCORE[0] // 2:
                self.screen.fill(k.COLOR_BLACK)
                COUNTING_SCORE[0] += FINAL_SCORE[0] / 1000
                GAME_SCORE[0] = PURGE_SERIF_175.render(k.display_score(COUNTING_SCORE[0]), True, k.COLOR_WHITE)
                self.screen.put_inside(JUDGEMENT_LABEL, k.JUDGEMENT_LABEL_POSITION)
                self.screen.put_inside(GAME_SCORE[0], k.GAME_SCORE_POSITION2)
                self.screen.update()
            self.screen.fill(k.COLOR_BLACK)
            COUNTING_SCORE[0] = FINAL_SCORE[0] // 2
            GAME_SCORE[0] = PURGE_SERIF_175.render(k.display_score(COUNTING_SCORE[0]), True, k.COLOR_WHITE)
            self.screen.put_inside(JUDGEMENT_LABEL, k.JUDGEMENT_LABEL_POSITION)
            self.screen.put_inside(GAME_SCORE[0], k.GAME_SCORE_POSITION2)
            self.screen.update()
            END_TIMERS[3].set_timer_seconds(1)
            END_TIMERS[3].activate()
            SFX_STORAGE['LOAD'].play()

        if END_TIMERS[3].ring():
            SFX_STORAGE['SHOOT'].play()
            if k.score_grade(FINAL_SCORE[0]) >= 'd':
                SFX_STORAGE['CHEER'].play()
            else:
                SFX_STORAGE['SCREAM'].play()

            self.screen.fill(k.COLOR_BLACK)
            COUNTING_SCORE[0] = FINAL_SCORE[0]
            PLAYER_GRADE[0] = PURGE_SERIF_415.render(k.score_grade(MIAUSMA.score), True, k.COLOR_YELLOW)
            GAME_SCORE[0] = PURGE_SERIF_175.render(k.display_score(FINAL_SCORE[0]), True, k.COLOR_WHITE)
            self.screen.put_inside(JUDGEMENT_LABEL, k.JUDGEMENT_LABEL_POSITION)
            self.screen.put_inside(PLAYER_GRADE[0], k.PLAYER_GRADE_POSITION2)
            self.screen.put_inside(GAME_SCORE[0], k.GAME_SCORE_POSITION2)
            END_TIMERS[4].set_timer_seconds(2)
            END_TIMERS[4].activate()

        if END_TIMERS[4].ring():
            self.screen.put_inside(RETURN_DIALOGUE, k.RETURN_DIALOGUE_POSITION)
            self.screen.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.gsm.set_state('main menu')

                if self.gsm.get_state() == MainMenu:
                    ABSTRACT_MINEFIELD.__init__(k.ABSTRACT_MINEFIELD_SIZE, k.ABSTRACT_MINEFIELD_DENSITY)
                    MINEFIELD.__init__(k.MINEFIELD_SIZE, k.MINEFIELD_POSITION, MOUSE, Interfaces.Tile, (k.MINEFIELD_SIZE[0] // k.ABSTRACT_MINEFIELD_SIZE[0], k.MINEFIELD_SIZE[1] // k.ABSTRACT_MINEFIELD_SIZE[1]), ABSTRACT_MINEFIELD)
                    MINEFIELD.fill_matrix()
                    MINEFIELD.set_damage_available()
                    MIAUSMA.wake()
                    MIAUSMA.set_animation('idle', k.set_proportion(2.14, 2.24), 7)
                    MIAUSMA.lives = k.MIAUSMA_LIVES
                    MIAUSMA.flags = k.MIAUSMA_FLAGS
                    MIAUSMA.set_current_speed([0, 0])
                    MIAUSMA.score = 0
                    MIAUSMA.multiplier = 1
                    MIAUSMA_REACTS_BASE[0] = 'normal'
                    MIAUSMA_REACTS.set_animation('normal', k.MIAUSMA_REACT_POSITION, 3)
                    GAME_SCORE[0] = PURGE_SERIF_175.render(k.display_score(MIAUSMA.score), True, k.COLOR_WHITE)
                    COUNTING_SCORE[0] = 0
                    FINAL_SCORE.pop()
                    self.screen.put_inside(BACKGROUND_MAIN_MENU, (0, 0))
                    PLAYLIST_MAIN_MENU.queue_shuffle()
                    PLAYLIST_MAIN_MENU.start()
                    break
