# pylint: skip-file
import unittest
from board import Board
from player import Player
from tile import OccupiedTile, InvalidTileTypeError

class TestPlayer(unittest.TestCase):

    def setUp(self):
        """ Configuración que se ejecuta antes de cada prueba """
        self.board = Board(3)
        self.player_x = Player("X")
        self.player_o = Player("O")

    def test_01_place_tile_valid_position(self):
        self.player_x.place_tile(self.board, 0)
        self.assertEqual(self.board[0], "X")

    def test_02_place_tile_invalid_position(self):
        with self.assertRaises(IndexError):
            self.player_x.place_tile(self.board, 9)

    def test_03_place_tile_position_already_occupied(self):
        self.player_x.place_tile(self.board, 1)
        with self.assertRaises(OccupiedTile):
            self.player_o.place_tile(self.board, 1)

    def test_04_invalid_tile_type(self):
        with self.assertRaises(InvalidTileTypeError):
            Player("A")

    def test_05_switch_player(self):
        initial_index = self.player_x._Player__current_player_index # type: ignore
        self.player_x.switch_player()
        self.assertEqual(self.player_x._Player__current_player_index, (initial_index + 1) % self.player_x._Player__player_quantity) # type: ignore
        self.player_x.switch_player()
        self.assertEqual(self.player_x._Player__current_player_index, initial_index) # type: ignore

    def test_06_place_tile_on_empty_board(self):
        self.player_x.place_tile(self.board, 4)
        self.assertEqual(self.board[4], "X")

    def test_07_place_tile_on_first_and_last_position(self):
        self.player_x.place_tile(self.board, 0)
        self.assertEqual(self.board[0], "X")
        self.player_x.place_tile(self.board, 8)
        self.assertEqual(self.board[8], "X")

if __name__ == '__main__':
    unittest.main()
