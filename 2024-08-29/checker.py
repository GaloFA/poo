# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from board import Board
from collection_handler import CollectionIterable


class Checker():
    """ Clase que verifica luego de cada 
    jugada si algun jugador ganó o empataron. """

    def __init__(self):
        pass

    def check_win_row(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador ( SOLO FILAS ) """
        dimensions = board.dimensions

        for row in range(dimensions):
            temp_list = CollectionIterable()
            row_start = row * dimensions

            for row_element in range(dimensions):
                tile_value = next(iter(board[row_start + row_element]))
                temp_list.append(tile_value)

            if temp_list.check_if_elements_inside_list_are_equal():
                return True

        return False

    def check_win_column(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador ( SOLO COLUMNAS ) """
        dimensions = board.dimensions

        for column in range(dimensions):
            temp_list = CollectionIterable()

            for column_element in range(dimensions):
                tile_value = next(iter(board[column_element * dimensions + column]))
                temp_list.append(tile_value)

            if temp_list.check_if_elements_inside_list_are_equal():
                return True

        return False

    def check_win_first_diagonal(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador 
        ( COLUMNA DE ARRIBA A LA IZQUIERDA HASTA ABAJO A LA DERECHA ) """
        dimensions = board.dimensions
        temp_list = CollectionIterable()

        for i in range(dimensions):
            tile_value = next(iter(board[i * (dimensions + 1)]))
            temp_list.append(tile_value)

        return temp_list.check_if_elements_inside_list_are_equal()

    def check_win_second_diagonal(self, board: Board):
        """ Método que verifica luego de cada jugada si hubo un ganador 
        ( COLUMNA DE ARRIBA A LA DERECHA HASTA ABAJO A LA IZQUIERDA ) """
        dimensions = board.dimensions
        temp_list = CollectionIterable()

        for i in range(dimensions):
            tile_value = next(iter(board[(i + 1) * (dimensions - 1)]))
            temp_list.append(tile_value)

        return temp_list.check_if_elements_inside_list_are_equal()

    def check_tie(self, board: Board):
        """Método que verifica si hubo un empate."""
        if self.check_win(board):
            return False

        return board.check_board_is_full()

    def check_win(self, board: Board):
        """ Método que se encarga de utilizar todos los otros métodos
        para que, en vez de tener que llamarlos uno por uno, poder
        llamar todos desde este mismo método. """

        return self.check_win_row(board) or self.check_win_column(board) or self.check_win_first_diagonal(board) or self.check_win_second_diagonal(board)
