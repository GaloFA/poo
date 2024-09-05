# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, attribute-defined-outside-init, protected-access
""" Imports """
from board import Board
from player import Player
from checker import Checker
import player_interaction


class Game():
    """ Clase que se encarga de correr el juego """

    def __init__(self, dimensions: int):
        self.reset(dimensions)

    def reset(self, dimensions: int):
        """ Método para reiniciar el juego con las dimensiones actuales """

        self._dimensions = dimensions
        self._board = Board(self._dimensions)
        self._players = [Player("X"), Player("O")]
        self._checker = Checker()
        self._current_player_index = 0
        self._interaction = player_interaction.PlayerInteraction()

    def run(self):
        """ Ejecutar el juego """

        running = True

        while running:
            if self.game_finished():
                running = self._interaction.play_again(self)
            else:
                self.play_turn()

    def game_finished(self):
        """ Método que maneja el final de una partida """

        self._board.render.print_board() # type: ignore

        if self._checker.check_tie(self._board):
            print("Empate!")
            return True

        if self._checker.check_win(self._board):
            winner = self._players[(self._current_player_index + 1) % 2]
            print(f"Ganó el jugador {winner.tile_type}!")
            return True

        return False

    def play_turn(self):
        """ Método que se encarga de manejar cada turno, printeando el tablero,
        haciendo la jugada del jugador y pasandole el turno al siguiente jugador """

        self._board.render.print_board() # Printear el tablero actual # type: ignore

        move = self._interaction.get_player_move(self._board, self._players[self._current_player_index]) # Obtener la jugada que hace el jugador

        self._players[self._current_player_index].place_tile(self._board, move) # Realizar el movimiento que eligió el jugador

        self._players[self._current_player_index].switch_player() # Turno nuevo, cambia el jugador que está jugando

        self._current_player_index = (self._current_player_index + 1) % 2 # Establece el jugador actual

    @property
    def get_game_instance(self):
        """ Retorna la instancia del juego """
        return self
