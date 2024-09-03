# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from board import Board

class Tile():
    """ Clase que representa a un casillero del
    tablero, además de permitirle designar una
    ficha (X o O) como "valor actual" """

    def __init__(self, board: Board):
        self.__board = board
        self.__max_index_value = self.__board.dimensions ** 2

    def change_tile(self, index: int, tile_type: str):
        """ Método que se encarga de cambiar la ficha en una determinada posición """
        if not (0 <= index < self.__max_index_value):
            raise InvalidPositionValueError("No se puede ingresar a una posición fuera del rango establecido")

        if tile_type not in ["X", "O"]:
            raise InvalidTileTypeError("El tipo de ficha debe ser 'O' o 'X'")

        self.__board[index] = tile_type

# Exceptions

class InvalidPositionValueError(Exception):
    """ Excepcion de valor de posición inválido """
    def __init__(self, message):
        pass

class InvalidTileTypeError(Exception):
    """ Excepción para tipo de ficha inválido """
    def __init__(self, message):
        super().__init__(message)
