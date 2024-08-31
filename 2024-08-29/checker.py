""" Imports """
from board import Board
from list_handler import ListHandler

class Checker():
    """ Clase que verifica luego de cada 
    jugada si algun jugador ganó o empataron. """

    def __init__(self):
        pass

    def check_win_row(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador ( SOLO FILAS ) """
        dimensions = board.get_board_dimensions()

        for row in range(dimensions):
            temp_list = ListHandler([])
            row_start = row * dimensions

            for row_element in range(dimensions):
                tile_value = board[row_start + row_element]
                temp_list.append(tile_value)

        return temp_list.check_if_elements_inside_list_are_equal()

    def check_win_column(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador ( SOLO COLUMNAS ) """
        dimensions = board.get_board_dimensions()

        for column in range(dimensions):
            temp_list = ListHandler([])

            for column_element in range(dimensions):
                tile_value = board[column_element * dimensions + column]
                temp_list.append(tile_value)

        return temp_list.check_if_elements_inside_list_are_equal()

c = Checker()
b = Board(3)

print(c.check_win_row(b))
print(c.check_win_column(b))
