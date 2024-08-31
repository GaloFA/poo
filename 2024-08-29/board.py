""" Imports """
from list_handler import ListHandler

class Board(list):
    """ Clase que representa al tablero de juego,
    guarda su estado y sus dimensiones. """

    def __init__(self, dimensions):
        self.__dimensions = dimensions
        self.__board_list = ListHandler(["▢"] * (dimensions ** 2))

    def __getitem__(self, index):
        return self.__board_list[index]

    def draw_board(self):
        """ Método que se encarga de dibujar el tablero """
        final_board = ""
        iterator = iter(self.__board_list)

        for _ in range(0, self.__dimensions ** 2, self.__dimensions):
            for _ in range(self.__dimensions):
                final_board += next(iterator) + "   "
            final_board += "\n"

        return final_board

    def get_board_list(self):
        """ Método para acceder a la lista interna del tablero """
        return self.__board_list.get_list()

    def get_board_dimensions(self):
        """ Método para acceder a las dimensiones del tablero """
        return self.__dimensions
