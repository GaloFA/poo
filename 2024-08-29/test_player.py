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

    def test_05_switch_player(self):
        player_x = Player("X")
        initial_index = player_x._Player__current_player_index # type: ignore

        player_x.switch_player()
        self.assertEqual(player_x._Player__current_player_index, (initial_index + 1) % player_x._Player__player_quantity) # type: ignore

        player_x.switch_player()
        self.assertEqual(player_x._Player__current_player_index, initial_index) # type: ignore

    def test_06_place_tile_on_empty_board(self):
        board = Board(3)
        player_x = Player("X")

        player_x.place_tile(board, 4)

        self.assertEqual(board[4], "X")

    def test_07_place_tile_on_first_and_last_position(self):
        board = Board(3)
        player_x = Player("X")

        player_x.place_tile(board, 0)
        self.assertEqual(board[0], "X")

        player_x.place_tile(board, 8)
        self.assertEqual(board[8], "X")


if __name__ == '__main__':
    unittest.main()
