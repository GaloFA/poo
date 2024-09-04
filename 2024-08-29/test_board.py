# pylint: skip-file
import unittest
from board import Board
from tile import Tile

class TestBoard(unittest.TestCase):

    def test_01_board_length(self):
        board = Board(3)

        board_list = board.board_list

        self.assertEqual(len(board_list), 9)
    
    def test_02_board_dimensions(self):
        board = Board(3)

        dim = board.dimensions

        self.assertEqual(dim, 3)

    def test_03_board_drawn(self):
        board = Board(3)

        board_list = board.board_list

        for cell in board_list:
            self.assertEqual(cell, "▢")

    def test_04_board_get_item(self):
        board = Board(3)

        element = board[0]

        self.assertEqual(element, "▢")

    def test_05_board_index_out_of_range_error(self):
        board = Board(3)

        with self.assertRaises(IndexError):
            _ = board[9]

    def test_06_board_draw(self):
        board = Board(3)

        expected_output = "▢   ▢   ▢   \n▢   ▢   ▢   \n▢   ▢   ▢   \n"

        self.assertEqual(board.__board_render.draw_board(), expected_output)

    def test_07_board_draw_dimensions_5(self):
        board = Board(5)

        expected_output = "▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n"

        self.assertEqual(board.__board_render.draw_board(), expected_output)

    def test_08_check_board_is_full_true(self):
        board = Board(3)
        tile = Tile(board)

        for i in range(9):
            tile.change_tile(i, "X")

        self.assertTrue(board.check_board_is_full())

    def test_09_check_board_is_full_false(self):
        board = Board(3)
        tile = Tile(board)

        tile.change_tile(0, "X")

        self.assertFalse(board.check_board_is_full())
    
    def test_10_board_set_item_index_out_of_range(self):
        board = Board(3)

        with self.assertRaises(IndexError):
            board[9] = "X"

    def test_11_board_set_item_invalid_tile_value(self):
        board = Board(3)

        with self.assertRaises(ValueError):
            board[0] = "A"
    
    def test_13_board_initialization(self):
        board = Board(4)
        
        self.assertEqual(board.dimensions, 4)
        self.assertEqual(len(board.board_list), 16)
        for i in range(board.dimensions):
            self.assertTrue(board[i] == "▢")

if __name__ == "__main__":
    unittest.main()
