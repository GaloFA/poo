# pylint: skip-file
import unittest
from board import Board
from tile import Tile

class TestBoard(unittest.TestCase):

    def setUp(self):
        """ Configuración que se ejecuta antes de cada prueba """
        self.board = Board(3)
        self.tile = Tile(self.board)

    def test_01_board_initialization(self):
        board = Board(3)
        self.assertEqual(board.dimensions, 3)
        self.assertEqual(len(board.board_list), 9)
        for i in range(board.dimensions ** 2):
            self.assertTrue(board[i] == "▢")

    def test_02_board_length(self):
        board_list = self.board.board_list
        self.assertEqual(len(board_list), 9)
    
    def test_03_board_dimensions(self):
        dim = self.board.dimensions
        self.assertEqual(dim, 3)

    def test_04_board_drawn(self):
        board_list = self.board.board_list
        for cell in board_list:
            self.assertEqual(cell, "▢")

    def test_05_board_get_item(self):
        element = self.board[0]
        self.assertEqual(element, "▢")

    def test_06_board_index_out_of_range_error(self):
        with self.assertRaises(IndexError):
            _ = self.board[9]

    def test_07_check_board_is_full_true(self):
        for i in range(9):
            self.tile.change_tile(i, "X")
        self.assertTrue(self.board.check_board_is_full())

    def test_08_check_board_is_full_false(self):
        self.tile.change_tile(0, "X")
        self.assertFalse(self.board.check_board_is_full())
    
    def test_09_board_set_item_index_out_of_range(self):
        with self.assertRaises(IndexError):
            self.board[9] = "X"

    def test_10_board_set_item_invalid_tile_value(self):
        with self.assertRaises(ValueError):
            self.board[0] = "A"

if __name__ == "__main__":
    unittest.main()
