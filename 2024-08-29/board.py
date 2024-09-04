# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from os import system
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

    def draw_reference_board(self):
        """ Tablero que se utiliza para dar una referencia del número
        de las posiciones de cada casillero en el tablero """
        reference_board = ""

        for row in range(self.__dimensions):
            for col in range(self.__dimensions):
                position = row * self.__dimensions + col # Representa la posición de cada casillero en el tablero
                reference_board += f"{position}   " # Agrega cada posición a un string y la formatea para que tenga formato de tablero
            reference_board += "\n"

        return reference_board # Retorna el tablero de referencia

    def draw_board(self):
        """ Método que se encarga de dibujar el tablero """
        final_board = ""
        iterator = iter(self.__board_list)

        for _ in range(0, self.__dimensions ** 2, self.__dimensions):
            for _ in range(self.__dimensions):
                final_board += f"{next(iterator)}   " # Genera el tablero en su estado actual
            final_board += "\n" # Agrega nuevas lineas para poner el formato de tablero correcto

        return final_board # Retorna el tablero en formato correcto

    def print_board(self):
        """ Método para imprimir el estado actual del tablero """
        system("cls")
        print("\n")
        print(self.draw_reference_board())
        print(self.draw_board())

    def check_board_is_full(self):
        """Método que verifica si todas las casillas del tablero están ocupadas."""

        for i in range(self.__dimensions ** 2):
            if self.__board_list[i] == "▢":
                return False
        return True

    @property
    def board_list(self):
        """ Getter de la lista del tablero """
        return self.__board_list.get_list()

    @property
    def dimensions(self):
        """ Getter de las dimensiones del tablero """
        return self.__dimensions
