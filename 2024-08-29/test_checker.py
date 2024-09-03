# pylint: skip-file
import unittest
from board import Board
from checker import Checker
from tile import Tile


class TestChecker(unittest.TestCase):
    def test_01_check_win_row_true(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(0, "X")
        tile.change_tile(1, "X")
        tile.change_tile(2, "X")

        self.assertTrue(checker.check_win_row(board))

    def test_02_check_win_row_false(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(0, "X")
        tile.change_tile(1, "X")
        tile.change_tile(2, "O")

        self.assertFalse(checker.check_win_row(board))

    def test_03_check_win_column_true(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(0, "X")
        tile.change_tile(3, "X")
        tile.change_tile(6, "X")

        self.assertTrue(checker.check_win_column(board))

    def test_04_check_win_column_false(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(0, "X")
        tile.change_tile(3, "X")
        tile.change_tile(6, "O")

        self.assertFalse(checker.check_win_column(board))

    def test_05_check_win_first_diagonal_true(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(0, "O")
        tile.change_tile(4, "O")
        tile.change_tile(8, "O")

        self.assertTrue(checker.check_win_first_diagonal(board))

    def test_06_check_win_first_diagonal_false(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(0, "O")
        tile.change_tile(4, "O")
        tile.change_tile(8, "X")

        self.assertFalse(checker.check_win_first_diagonal(board))

    def test_07_check_win_second_diagonal_true(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(2, "X")
        tile.change_tile(4, "X")
        tile.change_tile(6, "X")

        self.assertTrue(checker.check_win_second_diagonal(board))

    def test_08_check_win_second_diagonal_false(self):
        board = Board(3)
        checker = Checker()
        tile = Tile(board)

        tile.change_tile(2, "X")
        tile.change_tile(4, "X")
        tile.change_tile(6, "O")

        self.assertFalse(checker.check_win_second_diagonal(board))


if __name__ == '__main__':
    unittest.main()
