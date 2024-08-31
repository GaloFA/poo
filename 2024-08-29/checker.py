""" Imports """
from board import Board
from list_handler import ListHandler

class Checker():
    """ Clase que verifica luego de cada 
    jugada si algun jugador ganó o empataron. """

    def __init__(self):
        pass

    def check_win_row(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador """
        dimensions = board.get_board_dimensions()

        for row in range(dimensions):
            temp_list = ListHandler([])
            row_start = row * dimensions

            for row_element in range(dimensions):
                element = board[row_start + row_element]
                temp_list.append(element)

        return temp_list.check_if_elements_inside_list_are_equal()

c = Checker()
b = Board(3)

print(c.check_win_row(b))
