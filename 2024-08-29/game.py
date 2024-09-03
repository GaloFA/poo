# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, attribute-defined-outside-init
""" Imports """
from os import system
from board import Board
from player import Player
from checker import Checker

class Game():
    """ Clase que se encarga de correr el juego """

    def __init__(self, dimensions: int):
        self.reset(dimensions)

    def reset(self, dimensions: int):
        """ Método para reiniciar el juego con las dimensiones actuales """
        self.__dimensions = dimensions
        self.__board = Board(self.__dimensions)
        self.__players = [Player("X"), Player("O")]
        self.__checker = Checker()
        self.__current_player_index = 0

    def print_board(self):
        """ Método para imprimir el estado actual del tablero """
        system("cls")
        print(self.__board.draw_reference_board())
        print(self.__board.draw_board())

    def get_player_move(self):
        """ Método para obtener la jugada del jugador actual """
        move = None
        while move is None:
            try:
                move = int(input(f"Player {self.__players[self.__current_player_index].tile_type}, enter your move (0-{self.__board.dimensions ** 2 - 1}): "))
                if move < 0 or move >= self.__board.dimensions ** 2:
                    print("Jugada inválida. (Index out of range)")
                    move = None
                elif self.__board[move] != "▢":
                    print("Jugada inválida. Posición ya ocupada.")
                    move = None
            except ValueError:
                print("Input inválido. Hay que ingresar un número.")
        return move

    def run(self):
        """ Método del juego ejecutándose """
        running = True
        match_finished = False

        while running:
            if match_finished:
                print("Partida finalizada")
                response = input("¿Quiere seguir jugando? (s/n): ").lower()

                while response not in ["s", "n"]:
                    print("Respuesta inválida (s/n)")
                    response = input("¿Quiere seguir jugando? (s/n): ").lower()

                if response == 's':
                    self.reset(self.__dimensions)
                    match_finished = False
                else:
                    running = False
            else:
                self.print_board()
                move = self.get_player_move()
                self.__players[self.__current_player_index].place_tile(self.__board, move)

                if self.__checker.check_win_row(self.__board) or \
                   self.__checker.check_win_column(self.__board) or \
                   self.__checker.check_win_first_diagonal(self.__board) or \
                   self.__checker.check_win_second_diagonal(self.__board):
                    self.print_board()
                    print(f"Ganó el jugador {self.__players[self.__current_player_index].tile_type}!")
                    match_finished = True
                else:
                    self.__players[self.__current_player_index].switch_player()
                    self.__current_player_index = (self.__current_player_index + 1) % 2
