import pygame
import Game
import Interfaces
import Characters

if __name__ == '__main__':

    # TÍTULO DO JOGO, DIMENSÕES DA TELA E TAXA DE QUADROS
    GAME_TITLE = 'PyGame'
    SCREEN_DIMENSIONS = (720, 480)
    FPS = 60

    # ESTADOS E CLASSES DO ADMINISTRADOR DE ESTADOS
    BUNDLES = (('main menu', Game.MainMenu), ('main game', Game.MainGame))

    game = Game.Game(GAME_TITLE, SCREEN_DIMENSIONS, FPS)

    # CRIAÇÃO E INICIALIZAÇÃO DA TELA INICIAL E DO ADMINISTRADOR DE ESTADOS
    game.screen_init()
    game.gsm_init(BUNDLES, 'main menu')

    # INICIALIZAÇÃO DO JOGO
    game.run()
