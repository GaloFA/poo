# pylint: disable=line-too-long, superfluous-parens
""" Imports """
from board import Board

class Tile():
    """ Clase que representa a un casillero del
    tablero, además de permitirle designar una
    ficha (X o O) como "valor actual" """

    def __init__(self, board: Board, index: int):
        self.__board = board
        self.__position_value = board[index]
        self.__max_position_value = self.__board.dimensions() ** 2

    def change_tile(self, position: int, tile_type: str):
        """ Método que se encarga de cambiar la ficha en una determinada posición """
        if not (0 <= position < self.__max_position_value):
            raise InvalidPositionValueError("No se puede ingresar a una posición fuera del rango establecido")

        # Verificamos si el tipo de ficha es válido
        if tile_type not in ["X", "O"]:
            raise InvalidTileTypeError("El tipo de ficha debe ser 'O' o 'X'")

        # Cambiamos la ficha en la posición indicada
        self.__board.list()[position] = tile_type


# Exceptions

class InvalidPositionValueError(Exception):
    """ Excepcion de valor de posición inválido """
    def __init__(self, message):
        pass

class InvalidTileTypeError(Exception):
    """ Excepción para tipo de ficha inválido """
    def __init__(self, message):
        super().__init__(message)
