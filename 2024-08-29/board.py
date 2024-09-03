# pylint: disable=line-too-long, superfluous-parens
""" Imports """
from collection_handler import CollectionIterable

class Board(list):
    """ Clase que representa al tablero de juego,
    guarda su estado y sus dimensiones. """

    def __init__(self, dimensions):
        self.__dimensions = dimensions
        self.__board_list: CollectionIterable = CollectionIterable()

        for _ in range(dimensions ** 2):
            self.__board_list.append("▢")

    def __getitem__(self, index):
        return self.__board_list[index]

    def __setitem__(self, index, value):
        if not (0 <= index < self.__dimensions ** 2):
            raise IndexError("Index out of range")

        if value not in ["X", "O", "▢"]:
            raise ValueError("Invalid tile value")

        self.__board_list[index] = value

    def draw_board(self):
        """ Método que se encarga de dibujar el tablero """
        final_board = ""
        iterator = iter(self.__board_list)

        for _ in range(0, self.__dimensions ** 2, self.__dimensions):
            for _ in range(self.__dimensions):
                final_board += next(iterator) + "   "
            final_board += "\n"

        return final_board

    @property
    def board_list(self):
        """ Getter de la lista del tablero """
        return self.__board_list.get_list()

    @property
    def dimensions(self):
        """ Getter de las dimensiones del tablero """
        return self.__dimensions
