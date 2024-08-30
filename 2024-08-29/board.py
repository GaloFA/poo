""" Clases """

class Board():
    """ Clase que representa al tablero de juego,
    guarda su estado y sus dimensiones. """

    def __init__(self, dimensions):
        self.__dimensions = dimensions

    def draw_initial_board(self):
        """ Método que se encarga de dibujar el tablero inicial vacío """
        board = []
        for i in range(self.__dimensions):
            for t in range(self.__dimensions):
                board.append("▢")

    def draw_board(self):
        """ Método que se encarga de dibujar el tablero """
        board = Board(3)
        board.draw_initial_board()

        for i in range(0, self.__dimensions * self.__dimensions, 3):
            print(board[i] + "  | " + board[i + 1] + "  | " + board[i + 2]) #type: ignore

        return board

b = Board(3)

b.draw_board()
