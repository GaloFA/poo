# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from board import Board
from tile import Tile, InvalidTileTypeError, OccupiedTile

class Player():
    """ Clase de jugador que permite que se coloquen 
    fichas, además de manejar los turnos y el tipo de 
    ficha que tiene el jugador. """

    def __init__(self, tile_type: str):
        if tile_type not in ["X", "O"]:
            raise InvalidTileTypeError("El tipo de ficha debe ser 'X' o 'O'")
        self.tile_type = tile_type
        self.__current_player_index = 0
        self.__player_quantity = 2

    def place_tile(self, board: Board, position: int):
        """ Método para colocar una ficha en una posición específica del tablero """

        if not (0 <= position < board.dimensions ** 2):
            raise IndexError("La posición está fuera del rango del tablero")

        if board[position] != "▢":
            raise OccupiedTile("La posición ya está ocupada")

        tile = Tile(board)
        tile.change_tile(position, self.tile_type)

    def switch_player(self):
        """ Método para manejar turnos """

        self.__current_player_index = (self.__current_player_index + 1) % self.__player_quantity

    def get_player_move(self, board: Board):
        """ Método para obtener la jugada del jugador actual """
        move = None
        while move is None:
            try:
                move = int(input(f"Jugador {self.tile_type}, ingrese su jugada (0-{board.dimensions ** 2 - 1}): "))
                if move < 0 or move >= board.dimensions ** 2:
                    print("Jugada inválida. (Index out of range)")
                    move = None
                elif board[move] != "▢":
                    print("Jugada inválida. Posición ya ocupada.")
                    move = None
            except ValueError:
                print("Input inválido. Hay que ingresar un número.")
        return move
