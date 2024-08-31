""" Imports """
from board import Board

class Tile():
    """ Clase que representa a un casillero del
    tablero, además de permitirle designar una
    ficha (X o O) como "valor actual" """

    def __init__(self, position_value, board):
        self.__board = board
        self.__position_value = position_value
        self.__max_position_value = self.__board._Board__dimensions ** 2 # type: ignore

    def change_tile(self, board, position, tile_type):
        """ Método que se encarga de cambiar la ficha en una determinada posición """
        if self.__max_position_value < position or 0 > position:
            raise InvalidPositionValueError("No se puede ingresar a una posición fuera del rango establecido") # pylint: disable=line-too-long
        board[position] = tile_type

# Exceptions

class InvalidPositionValueError(Exception):
    """ Excepcion de valor de posición inválido """
    def __init__(self, message):
        pass
