# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-private-member
""" Imports """
from collection_handler import CollectionIterable
from board_render import BoardRender

class Board(list):
    """ Clase que representa al tablero de juego,
    guarda su estado y sus dimensiones. """

    def __init__(self, dimensions: int):
        self._dimensions = dimensions
        self._board_list: CollectionIterable = CollectionIterable()
        self._board_render: BoardRender = BoardRender(self)

        for _ in range(dimensions ** 2):
            self._board_list.append("▢")

    def __getitem__(self, index):
        return self._board_list[index]

    def __setitem__(self, index, value):
        if not (0 <= index < self._dimensions ** 2):
            raise IndexError("Index out of range")

        if value not in ["X", "O", "▢"]:
            raise ValueError("Invalid tile value")

        self._board_list[index] = value

    def check_board_is_full(self):
        """Método que verifica si todas las casillas del tablero están ocupadas."""

        for i in range(self._dimensions ** 2):
            if self._board_list[i] == "▢":
                return False

        return True

    @property
    def board_list(self):
        """ Getter de la lista del tablero """

        return self._board_list.get_list

    @property
    def dimensions(self):
        """ Getter de las dimensiones del tablero """

        return self._dimensions

    @property
    def render(self):
        """ Getter del board_render """

        return self._board_render
