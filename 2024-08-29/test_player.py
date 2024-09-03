# pylint: skip-file
import unittest
from board import Board
from player import Player
from tile import OccupiedTile, InvalidTileTypeError

class TestPlayer(unittest.TestCase):
    def test_01_place_tile_valid_position(self):
        board = Board(3)
        player_x = Player("X")
        player_o = Player("O")

        player_x.place_tile(board, 0)

        self.assertEqual(board[0], "X")

    def test_02_place_tile_invalid_position(self):
        board = Board(3)
        player_x = Player("X")
        player_o = Player("O")

        with self.assertRaises(IndexError):
            player_x.place_tile(board, 9)

    def test_03_place_tile_position_already_occupied(self):
        board = Board(3)
        player_x = Player("X")
        player_o = Player("O")

        player_x.place_tile(board, 1)

        with self.assertRaises(OccupiedTile):
            player_o.place_tile(board, 1)

    def test_04_invalid_tile_type(self):
        board = Board(3)

        with self.assertRaises(InvalidTileTypeError):
            Player("A")

if __name__ == '__main__':
    unittest.main()
