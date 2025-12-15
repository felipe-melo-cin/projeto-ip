from random import shuffle

class AbstractMinefield:

    def __init__(self, size, density):
        self.size = size
        self.width, self.height = size
        self.minefield = [[] for _ in range(self.height)]
        self.minefield_mask = [[] for _ in range(self.height)]
        self.minefield_interface = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.tiles = self.width * self.height
        self.bombs = int(self.tiles * density)
        self.free_tiles = self.tiles - self.bombs
        self.discovered_tiles = 0
        self.win = self.trip = False
        self.first_dig = True

    def fill_minefield(self):
        # PREENCHE UMA LISTA COM ESPAÇOS LIVRES (0) E BOMBAS (1)
        shallow_minefield = self.free_tiles * [0] + self.bombs * [1]

        # EMBARALHA-SE A LISTA
        shuffle(shallow_minefield)

        # TRANSFORMA-SE A LISTA EM UMA MATRIZ BIDIMENSIONAL
        self.minefield = [[] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                self.minefield[i].append(shallow_minefield[i * self.height + j])

    # CONTA QUANTAS BOMBAS HÁ AO REDOR DE UM LADRILHO
    def count_tile(self, tile):
        i_tile, j_tile = tile
        count = 0
        for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            if self.height > i_tile + i >= 0 and self.width > j_tile + j >= 0 and self.minefield[i_tile + i][j_tile + j]:
                count += 1
        self.minefield_mask[i_tile].append(count)

    # FAZ A CONTAGEM DE BOMBAS PARA CADA LADRILHO NO CAMPO MINADO
    def count_all(self):
        for i in range(self.height):
            for j in range(self.width):
                self.count_tile((i, j))

    # REVELA UM LADRILHO NO CAMPO MINADO
    def dig(self, tile, primary_dig=True):

        # COORDENADAS DO LADRILHO
        i_tile, j_tile = tile

        # SÓ REVELA O LADRILHO SE NÃO HOUVER UMA BANDEIRA
        if not (self.minefield_interface[i_tile][j_tile] == 2 and primary_dig):

            # É IMPOSSÍVEL ERRAR NA PRIMEIRA ESCAVAÇÃO
            if self.first_dig:
                self.first_dig = False

                # A PRIMEIRA ESCAVAÇÃO ACERTOU UMA BOMBA
                if self.minefield[i_tile][j_tile]:
                    self.minefield[i_tile][j_tile] = 0
                    self.minefield_interface[i_tile][j_tile] = 1
                    self.bombs -= 1
                    self.free_tiles += 1
                    self.discovered_tiles += 1
                    self.count_all()

                # A PRIMEIRA ESCAVAÇÃO ACERTOU UM LADRILHO LIVRE
                else:
                    self.count_all()
                    self.minefield_interface[i_tile][j_tile] = 1
                    self.discovered_tiles += 1

                # OS LADRILHOS AO REDOR SERÃO ESCAVADOS CASO NÃO HAJAM BOMBAS POR PERTO
                for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if self.height > i_tile + i >= 0 and self.width > j_tile + j >= 0 and self.minefield_interface[i_tile + i][j_tile + j] != 1 and not self.minefield_mask[i_tile][j_tile]:
                        self.dig((i_tile + i, j_tile + j), False)

            # ACERTOU UMA MINA SEM SER A PRIMEIRA ESCAVAÇÃO
            elif self.minefield[i_tile][j_tile]:
                self.trip = True

            # REVELOU UM LADRILHO SEM SER A PRIMEIRA ESCAVAÇÃO
            else:
                self.minefield_interface[i_tile][j_tile] = 1
                self.discovered_tiles += 1
                for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if self.height > i_tile + i >= 0 and self.width > j_tile + j >= 0 and self.minefield_interface[i_tile + i][j_tile + j] != 1 and not self.minefield_mask[i_tile][j_tile]:
                        self.dig((i_tile + i, j_tile + j), False)

    # INSERE UMA BANDEIRA NO CAMPO MINADO
    def flag(self, tile):
        i_tile, j_tile = tile
        view = self.minefield_interface[i_tile][j_tile]

        if view == 0:
            self.minefield_interface[i_tile][j_tile] = 2
        elif view == 2:
            self.minefield_interface[i_tile][j_tile] = 0

    # REINICIA O INDICADOR DE ERRO
    def reset_trip(self):
        self.trip = False
