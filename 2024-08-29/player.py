# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from board import Board
from tile import Tile

class Player():
    """ Clase de jugador que permite que se coloquen 
    fichas, además de manejar los turnos y el tipo de 
    ficha que tiene el jugador. """

    def __init__(self, tile_type: str):
        if tile_type not in ["X", "O"]:
            raise ValueError("El tipo de ficha debe ser 'X' o 'O'")
        self.tile_type = tile_type

    def place_tile(self, board: Board, position: int):
        """ Método para colocar una ficha en una posición específica del tablero """

        if not (0 < position <= board.dimensions ** 2):
            raise IndexError("La posición está fuera del rango del tablero")

        if board[position] != "▢":
            raise ValueError("La posición ya está ocupada")

        tile = Tile(board)
        tile.change_tile(position, self.tile_type)
