import pygame

# TÍTULO DO JOGO, DIMENSÕES DA TELA E TAXA DE QUADROS
GAME_TITLE = 'PURGATÓRIO'
SCREEN_DIMENSIONS = (1920, 1080)
FPS = 60

# DIMENSÕES DA TELA
SCREEN_WIDTH, SCREEN_HEIGHT = SCREEN_DIMENSIONS

# CARACTERÍSTICAS DO PROTAGONISTA
MIAUSMA_LIVES = 7
MIAUSMA_FLAGS = 10
MIAUSMA_SIZE = (112, 112)
MIAUSMA_MAX_SPEED = 5
MIAUSMA_ACC = 0.3
MIAUSMA_DAMPEN = 0.1
MIAUSMA_CDAMP = 0.2

# RNG DOS COLETÁVEIS (1 EM X)
RNG_LIFE_COLLECTABLE = 20
RNG_TIME_COLLECTABLE = 40
RNG_FLAG_COLLECTABLE = 10

# TAMANHO DAS BANDEIRAS
SIZE_FLAGS = (200, 200)

# LIMITE DE BANDEIRAS
FLAG_LIMIT = 8

# TAMANHO E TEMPO DE VIDA DOS COLETÁVEIS
SIZE_COLLECTABLES = (100, 100)
LIFETIME_COLLECTABLES = 3

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
COLOR_RED = (224, 0, 0)
COLOR_DARK_YELLOW = (240, 240, 64)
COLOR_YELLOW = (255, 255, 64)
COLOR_WHITE = (255, 255, 255)

# EVENTOS
RING_EVENT = pygame.event.custom_type()
MINESWEEPER_WIN = pygame.event.custom_type()
MINESWEEPER_PRIMARY_HIT = pygame.event.custom_type()
MINESWEEPER_HIT = pygame.event.custom_type()
MINESWEEPER_MISS = pygame.event.custom_type()
MINESWEEPER_FLAG = pygame.event.custom_type()
MINESWEEPER_UNFLAG = pygame.event.custom_type()

# ESPESSURAS
TILE_WIDTH = 7
NUMBER_WIDTH = 10

# PROPORÇÕES DA TELA
def set_proportion(scale_x, scale_y):
    return SCREEN_WIDTH // scale_x, SCREEN_HEIGHT // scale_y

# PROPORÇÕES DOS BOTÕES
TO_MAIN_GAME_BUTTON_SIZE = set_proportion(5.8, 15)
TO_MAIN_GAME_BUTTON_POSITION = set_proportion(2.43, 1.35)

QUIT_GAME_BUTTON_SIZE = set_proportion(5.8, 15)
QUIT_GAME_BUTTON_POSITION = set_proportion(2.43, 1.2)

# DEFINIÇÕES DO CAMPO MINADO ABSTRATO
ABSTRACT_MINEFIELD_SIZE = (10, 10)
ABSTRACT_MINEFIELD_DENSITY = 0.15

# PROPORÇÕES DO CAMPO MINADO
MINEFIELD_SIZE = set_proportion((16/9), 1)
MINEFIELD_POSITION = set_proportion(4.55, 10000)

# REDIMENSIONAMENTO DE IMAGENS
def resize_image(scale, source):
    image = pygame.image.load(source)
    resize = pygame.transform.scale(image, scale)
    return resize

def resize_images(scale, bundle):
    resized_bundle = []
    for source in bundle:
        image = pygame.image.load(source)
        resize = pygame.transform.smoothscale(image, scale)
        resized_bundle.append(resize)
    return resized_bundle
