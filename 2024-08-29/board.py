""" Clases """

class Board():
    """ Clase que representa al tablero de juego,
    guarda su estado y sus dimensiones. """

    def __init__(self, dimensions):
        self.__dimensions = dimensions

    def draw_initial_board(self):
        """ Método que se encarga de dibujar el tablero inicial vacío """
        drawn_board = []
        for i in range(self.__dimensions):
            for t in range(self.__dimensions):
                drawn_board.append("▢")
        return drawn_board

    def draw_board(self, board):
        """ Método que se encarga de dibujar el tablero """
        board = Board(3)
        drawn_board = board.draw_initial_board()
        final_board = ""

        for i in range(0, self.__dimensions * self.__dimensions, self.__dimensions):
            for t in range(self.__dimensions):
                final_board += drawn_board[t] + "   "
            print(final_board) # pylint: disable=line-too-long
            final_board = ""

        return final_board

b = Board(5)

b.draw_board(b)
