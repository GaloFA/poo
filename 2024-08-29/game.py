# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, attribute-defined-outside-init, protected-access
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
        """ Ejecutar el juego """

        running = True

        while running:
            if self.game_finished():
                running = self.play_again()
            else:
                self.play_turn()

    def game_finished(self):
        """ Método que maneja el final de una partida """

        self.__board.render.print_board() # type: ignore

        if self.__checker.check_tie(self.__board):
            print("Empate!")
            return True

        if self.__checker.check_win(self.__board):
            winner = self.__players[(self.__current_player_index + 1) % 2]
            print(f"Ganó el jugador {winner.tile_type}!")
            return True

        return False

    def play_again(self):
        """ Método que regunta si el usuario quiere seguir jugando """

        response = input("¿Quiere seguir jugando? (s/n): ").lower()

        while response not in ["s", "n"]:
            print("Respuesta inválida (s/n)")
            response = input("¿Quiere seguir jugando? (s/n): ").lower()

        if response == "s":
            self.reset(self.__dimensions)
            return True

        return False

    def play_turn(self):
        """ Método que se encarga de manejar cada turno, printeando el tablero,
        haciendo la jugada del jugador y pasandole el turno al siguiente jugador """

        self.__board.render.print_board() # Printear el tablero actual # type: ignore

        move = self.__players[self.__current_player_index].get_player_move(self.__board) # Obtener la jugada que hace el jugador

        self.__players[self.__current_player_index].place_tile(self.__board, move) # Realizar el movimiento que eligió el jugador

        self.__players[self.__current_player_index].switch_player() # Turno nuevo, cambia el jugador que está jugando

        self.__current_player_index = (self.__current_player_index + 1) % 2 # Establece el jugador actual
