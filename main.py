import Game
from Constantes import GAME_TITLE, SCREEN_DIMENSIONS, FPS

if __name__ == '__main__':

    # ESTADOS E CLASSES DO ADMINISTRADOR DE ESTADOS
    BUNDLES = (('main menu', Game.MainMenu), ('main game', Game.MainGame))

    # INICIALIZANDO O JOGO
    game = Game.Game(GAME_TITLE, SCREEN_DIMENSIONS, FPS)

    # CRIAÇÃO E INICIALIZAÇÃO DO ADMINISTRADOR DE ESTADOS
    game.gsm_init(BUNDLES, 'main menu')

    # INICIALIZAÇÃO DO JOGO
    game.run()
