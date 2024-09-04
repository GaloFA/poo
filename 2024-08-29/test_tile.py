# pylint: skip-file
import unittest
from board import Board
from tile import Tile, InvalidPositionValueError, InvalidTileTypeError

class TestTile(unittest.TestCase):

    def setUp(self):
        """ Configuración que se ejecuta antes de cada prueba """
        self.board = Board(3)
        self.tile = Tile(self.board)

    def test_01_change_tile_valid_position(self):
        self.tile.change_tile(0, "X")
        self.assertEqual(self.board.board_list[0], "X")

    def test_02_change_tile_invalid_position(self):
        with self.assertRaises(InvalidPositionValueError):
            self.tile.change_tile(9, "X")

        with self.assertRaises(InvalidPositionValueError):
            self.tile.change_tile(-1, "X")

    def test_03_change_tile_invalid_type(self):
        with self.assertRaises(InvalidTileTypeError):
            self.tile.change_tile(0, "A")

        with self.assertRaises(InvalidTileTypeError):
            self.tile.change_tile(0, "")

if __name__ == "__main__":
    unittest.main()
