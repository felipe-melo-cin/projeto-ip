import pygame

# ADAPTAÇÃO DAS DIMENSÕES À ESCALA FORNECIDA
def adapt_display_dimensions(scale, dimensions):
    scale_w, scale_h = scale
    width, height = dimensions
    if width // scale_w > height // scale_h:
        adapted_dimensions = (height // scale_h) * scale_w, height
    else:
        adapted_dimensions = width, (width // scale_w) * scale_h
    return adapted_dimensions

# PROPORÇÕES RELATIVAS À TELA
def set_proportion(scale_x, scale_y):
    return SCREEN_WIDTH // scale_x, SCREEN_HEIGHT // scale_y

# PROPORÇÕES RELATIVAS À TELA (VALORES DE PONTO FLUTUANTE)
def set_proportion_float(scale_x, scale_y):
    return SCREEN_WIDTH / scale_x, SCREEN_HEIGHT / scale_y

# TÍTULO DO JOGO
GAME_TITLE = 'PURGATÓRIO'

# DIMENSÕES DA TELA
pygame.display.init()
SCREEN_INFO = pygame.display.Info()
SCREEN_DIMENSIONS_RAW = SCREEN_INFO.current_w, SCREEN_INFO.current_h
SCREEN_DIMENSIONS = adapt_display_dimensions((16, 9), SCREEN_DIMENSIONS_RAW)

# TAXA DE QUADROS
FPS = 60

# DIMENSÕES DA TELA
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_DIMENSIONS

# TAMANHO DAS FONTES
FONT_SIZE_PURGE_SERIF_175 = int(max(set_proportion(10.9714, 10.9714)))
FONT_SIZE_PURGE_SERIF_180 = int(max(set_proportion(10.6666, 10.6666)))
FONT_SIZE_PURGE_SERIF_415 = int(max(set_proportion(4.6265, 4.6265)))

FONT_SIZE_FUZZY_BUBBLES_40 = max(set_proportion(48, 48))
FONT_SIZE_FUZZY_BUBBLES_60 = max(set_proportion(32, 32))
FONT_SIZE_FUZZY_BUBBLES_80 = max(set_proportion(24, 24))

# MÚSICAS
VOLUME_BGM = 0.1
PLAYLIST_MAIN_MENU_MUSICS = [
    'Audio/bgm/mainmenu0.ogg',
    'Audio/bgm/mainmenu1.ogg'
]
PLAYLIST_MAIN_GAME_MUSICS = [
    'Audio/bgm/soundtrack0.ogg',
    'Audio/bgm/soundtrack1.ogg',
    'Audio/bgm/soundtrack2.ogg',
    'Audio/bgm/soundtrack3.ogg'
]

# EFEITOS SONOROS
VOLUME_SFX = 0.2

# DEFINIÇÕES DO CAMPO MINADO ABSTRATO
ABSTRACT_MINEFIELD_SIZE = (10, 10)
ABSTRACT_MINEFIELD_DENSITY = 0.12

# PROPORÇÕES DO CAMPO MINADO
MINEFIELD_SIZE = set_proportion((16/9), 1)
MINEFIELD_POSITION = set_proportion(4.5714, 10000)

# TEMPO LIMITE DE JOGO
TIME_LIMIT_SECONDS = 60

# CARACTERÍSTICAS DO PROTAGONISTA
MIAUSMA_SIZE = set_proportion((16/9) * ABSTRACT_MINEFIELD_SIZE[0], 1 * ABSTRACT_MINEFIELD_SIZE[1])
MIAUSMA_LIVES = 7
MIAUSMA_FLAGS = 10
MIAUSMA_MAX_SPEED = max(set_proportion(320, 320))
MIAUSMA_ACC = max(set_proportion_float(4800, 4800))
MIAUSMA_DAMPEN = max(set_proportion_float(19200, 19200))
MIAUSMA_CDAMP = max(set_proportion_float(9600, 9600))
MIAUSMA_RANGE = 2

# REAÇÕES DO PROTAGONISTA
MIAUSMA_REACT_SIZE = set_proportion(4.5714, 2.4814)
MIAUSMA_REACT_POSITION = set_proportion(10000, 1.67)

# CARACTERÍSTICAS DOS TEXTOS NA TELA DO JOGO
PLAYER_GRADE_POSITION = set_proportion(10000, 10000)
PLAYER_GRADE_POSITION2 = set_proportion(2.6, 4)
GAME_SCORE_POSITION = set_proportion(10000, 3)
GAME_SCORE_POSITION2 = set_proportion(2.6, 2)
GAME_SCORE_LABEL_POSITION = set_proportion(100, 2.2)
GAME_MULTIPLIER_POSITION = set_proportion(6.5, 2.25)
TIME_LEFT_LABEL_POSITION = set_proportion(1.25, 6.2)
JUDGEMENT_TIME_LABEL_POSITION = set_proportion(4, 6)
JUDGEMENT_LABEL_POSITION = set_proportion(2.55, 6)
PAUSE_DIALOGUE_POSITION = set_proportion(5.95, 2.5)
RETURN_DIALOGUE_POSITION = set_proportion(4.8, 1.2)

# CARACTERÍSTICAS DO TEMPO RESTANTE
TIME_LEFT_POSITION = set_proportion(1.26, 5)

# CARACTERÍSTICAS DO CONTADOR DE BANDEIRA
FLAG_COUNTER_POSITION = set_proportion(1.26, 2.6)

# CARACTERÍSTICAS DO ÍCONE DE BANDEIRA
FLAG_ICON_SIZE = set_proportion(12.8, 7.2)
FLAG_ICON_POSITION = set_proportion(1.08, 3)

# CARACTERÍSTICAS DO PLACAR DE VIDA
LIFE_DISPLAY_SIZE = set_proportion(4.5714, 1.9918)
LIFE_DISPLAY_POSITION = set_proportion(1.28, 2.0082)

# CARACTERÍSTICAS DAS VIDAS NO PLACAR DE VIDA
LIFE_ICON_SIZE = set_proportion(25.9459, 15.8823)
LIFE_ICONS_POSITION = [
    set_proportion(1.15, 1.6),
    set_proportion(1.22, 1.475),
    set_proportion(1.088, 1.475),
    set_proportion(1.15, 1.375),
    set_proportion(1.22, 1.265),
    set_proportion(1.088, 1.265),
    set_proportion(1.15, 1.2)
]

# RNG DOS COLETÁVEIS (1 EM X)
RNG_LIFE_COLLECTABLE = 20
RNG_TIME_COLLECTABLE = 40
RNG_FLAG_COLLECTABLE = 10

# TAMANHO DAS BANDEIRAS E DAS BOMBAS
SIZE_FLAGS = set_proportion(9.6, 5.4)
SIZE_BOMBS = set_proportion(9.6, 5.4)

# TEMPO FORNECIDO PELO COLETÁVEL DE TEMPO
TIME_COLLECTABLE_BONUS = 3

# LIMITE DE BANDEIRAS
FLAG_LIMIT = 20

# TAMANHO E TEMPO DE VIDA DOS COLETÁVEIS
SIZE_COLLECTABLES = set_proportion(19.2, 10.8)
LIFETIME_COLLECTABLES = 5

# CORES
COLOR_BLACK = (0, 0, 0)
COLOR_DARK_BLUE = (0, 0, 96)
COLOR_BLUE = (0, 0, 160)
COLOR_DARK_GREEN = (0, 96, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_LIGHT_GREEN = (0, 160, 0)
COLOR_DARK_PURPLE = (32, 0, 32)
COLOR_PURPLE = (64, 0, 64)
COLOR_DARK_GRAY = (64, 64, 64)
COLOR_TEAL = (64, 160, 160)
COLOR_MAROON = (128, 0, 0)
COLOR_GRAY = (128, 128, 128)
COLOR_DARK_RED = (192, 0, 0)
COLOR_DARK_YELLOW = (192, 192, 0)
COLOR_RED = (224, 0, 0)
COLOR_PALE_DARK_YELLOW = (240, 240, 64)
COLOR_YELLOW = (255, 255, 0)
COLOR_PALE_YELLOW = (255, 255, 64)
COLOR_WHITE = (255, 255, 255)

# CORES TRANSPARENTES
COLOR_ALPHA32_YELLOW = (255, 255, 0, 32)

# EVENTOS
TO_MAIN_GAME_TRANSITION = pygame.event.custom_type()
BUTTON_HOVER = pygame.event.custom_type()
GAME_START = pygame.event.custom_type()
GAME_PAUSE = pygame.event.custom_type()
GET_COLLECTABLE = pygame.event.custom_type()
DAMAGE_PLAYER = pygame.event.custom_type()
OVERHEAL = pygame.event.custom_type()
OVERFLAG = pygame.event.custom_type()
MUSIC_END = pygame.event.custom_type()
GAME_OVER = pygame.event.custom_type()
MINESWEEPER_WIN = pygame.event.custom_type()
MINESWEEPER_PRIMARY_HIT = pygame.event.custom_type()
MINESWEEPER_HIT = pygame.event.custom_type()
MINESWEEPER_FLAG = pygame.event.custom_type()
MINESWEEPER_UNFLAG = pygame.event.custom_type()
MINESWEEPER_MISS = pygame.event.custom_type()

# ESPESSURAS
TILE_WIDTH = max(set_proportion(200, 200))
NUMBER_WIDTH = max(set_proportion(150, 150))

# TAMANHO DAS IMAGENS DOS BOTÕES
TO_MAIN_GAME_BUTTON_MASK_SIZE = set_proportion(5.8, 15)
QUIT_GAME_BUTTON_MASK_SIZE = set_proportion(5.8, 15)

# PROPORÇÕES DOS BOTÕES
TO_MAIN_GAME_BUTTON_SIZE = set_proportion(5.8, 15)
TO_MAIN_GAME_BUTTON_POSITION = set_proportion(2.43, 1.35)

QUIT_GAME_BUTTON_SIZE = set_proportion(5.8, 15)
QUIT_GAME_BUTTON_POSITION = set_proportion(2.43, 1.2)

PAUSE_BUTTON_SIZE = set_proportion(4.5714, 10)
PAUSE_BUTTON_POSITION = set_proportion(1.28, 10000)
PAUSE_BUTTON_BORDER_WIDTH = max(set_proportion(200, 200))
PAUSE_BUTTON_BORDER_RADIUS = max(set_proportion(100, 100))

# REDIMENSIONAMENTO DE IMAGENS
def resize_image(scale, source):
    image = pygame.image.load(source)
    resize = pygame.transform.smoothscale(image, scale).convert_alpha()
    return resize.convert_alpha()

def resize_images(scale, bundle):
    resized_bundle = []
    for source in bundle:
        image = pygame.image.load(source)
        resize = pygame.transform.smoothscale(image, scale).convert_alpha()
        resized_bundle.append(resize)
    return resized_bundle

# MOSTRAR VALORES NA TELA
def display_score(score):
    if score > 99999:
        score = 99999
    return f'{int(score):0>5}'

def display_multiplier(multiplier):
    return f'x{multiplier}'

def display_out_of(value, limit):
    return f'{value}/{limit}'

def time_milliseconds_to_display(time):
    time = time // 1000
    return f'{time // 60:0>2}:{time % 60:0>2}'

# CALCULAR NOTA DO PLAYER
def score_grade(score):
    if score < 2000:
        return 'a'
    elif score < 4000:
        return 'b'
    elif score < 8000:
        return 'c'
    elif score < 16000:
        return 'd'
    elif score < 32000:
        return 'e'
    else:
        return 'f'
