""" Clases """
from board import Board

class Checker():
    """ Clase que verifica luego de cada 
    jugada si algun jugador ganó o empataron. """

    def __init__(self):
        pass

    def check_win(self):
        """ Método que verifica luego de cada jugada si hubo un ganador """

        board = Board
        rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        columns = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        diagonals = [(1, 5, 9), (3, 5, 7)]
        position = 1 # starting position

        for tile in range(position, 10, 3):
            print(tile, position)
            if tile >= 7:
                position += 1
                tile = position
                print(f"inside if: {tile, position}")
            print(tile,position)

c = Checker()

c.check_win()
