# pylint: skip-file
import unittest
from board import Board
from tile import Tile, InvalidPositionValueError, InvalidTileTypeError

class TestTile(unittest.TestCase):

    def test_01_change_tile_valid_position(self):
        board = Board(3)
        tile = Tile(board)

        tile.change_tile(0, "X")

        self.assertEqual(board.board_list[0], "X")

    def test_02_change_tile_invalid_position(self):
        board = Board(3)
        tile = Tile(board)

        with self.assertRaises(InvalidPositionValueError):
            tile.change_tile(9, "X")

        with self.assertRaises(InvalidPositionValueError):
            tile.change_tile(-1, "X")

    def test_03_change_tile_invalid_type(self):
        board = Board(3)
        tile = Tile(board)

        with self.assertRaises(InvalidTileTypeError):
            tile.change_tile(0, "A")

        with self.assertRaises(InvalidTileTypeError):
            tile.change_tile(0, "")

if __name__ == "__main__":
    unittest.main()
