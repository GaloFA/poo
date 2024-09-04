# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, attribute-defined-outside-init
""" Imports """
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
                self.__board.print_board()
                move = self.__players[self.__current_player_index].get_player_move(
                    self.__board)
                self.__players[self.__current_player_index].place_tile(
                    self.__board, move)

                if self.__checker.check_tie(self.__board):
                    self.__board.print_board()
                    print("Empate!")
                    match_finished = True

                if self.__checker.check_win(self.__board):
                    self.__board.print_board()
                    print(f"Ganó el jugador {
                          self.__players[self.__current_player_index].tile_type}!")
                    match_finished = True
                else:
                    self.__players[self.__current_player_index].switch_player()
                    self.__current_player_index = (
                        self.__current_player_index + 1) % 2
