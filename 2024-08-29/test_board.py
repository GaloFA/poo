# pylint: skip-file
import unittest
from board import Board


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

        self.assertEqual(board.draw_board(), expected_output)

    def test_07_board_draw_dimensions_5(self):
        board = Board(5)

        expected_output = "▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n"

        self.assertEqual(board.draw_board(), expected_output)

if __name__ == "__main__":
    unittest.main()
