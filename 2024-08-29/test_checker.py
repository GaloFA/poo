# pylint: skip-file
import unittest
from board import Board
from checker import Checker
from tile import Tile

class TestChecker(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)
        self.checker = Checker()
        self.tile = Tile(self.board)

    def test_01_check_win_row_true(self):
        self.tile.change_tile(0, "X")
        self.tile.change_tile(1, "X")
        self.tile.change_tile(2, "X")

        self.assertTrue(self.checker.check_win_row(self.board))

    def test_02_check_win_row_false(self):
        self.tile.change_tile(0, "X")
        self.tile.change_tile(1, "X")
        self.tile.change_tile(2, "O")

        self.assertFalse(self.checker.check_win_row(self.board))

    def test_03_check_win_column_true(self):
        self.tile.change_tile(0, "X")
        self.tile.change_tile(3, "X")
        self.tile.change_tile(6, "X")

        self.assertTrue(self.checker.check_win_column(self.board))

    def test_04_check_win_column_false(self):
        self.tile.change_tile(0, "X")
        self.tile.change_tile(3, "X")
        self.tile.change_tile(6, "O")

        self.assertFalse(self.checker.check_win_column(self.board))

    def test_05_check_win_first_diagonal_true(self):
        self.tile.change_tile(0, "O")
        self.tile.change_tile(4, "O")
        self.tile.change_tile(8, "O")

        self.assertTrue(self.checker.check_win_first_diagonal(self.board))

    def test_06_check_win_first_diagonal_false(self):
        self.tile.change_tile(0, "O")
        self.tile.change_tile(4, "O")
        self.tile.change_tile(8, "X")

        self.assertFalse(self.checker.check_win_first_diagonal(self.board))

    def test_07_check_win_second_diagonal_true(self):
        self.tile.change_tile(2, "X")
        self.tile.change_tile(4, "X")
        self.tile.change_tile(6, "X")

        self.assertTrue(self.checker.check_win_second_diagonal(self.board))

    def test_08_check_win_second_diagonal_false(self):
        self.tile.change_tile(2, "X")
        self.tile.change_tile(4, "X")
        self.tile.change_tile(6, "O")

        self.assertFalse(self.checker.check_win_second_diagonal(self.board))
    
    def test_09_check_tie_true(self):
        self.tile.change_tile(0, "X")
        self.tile.change_tile(1, "O")
        self.tile.change_tile(2, "X")
        self.tile.change_tile(3, "X")
        self.tile.change_tile(4, "O")
        self.tile.change_tile(5, "X")
        self.tile.change_tile(6, "O")
        self.tile.change_tile(7, "X")
        self.tile.change_tile(8, "O")

        self.assertTrue(self.checker.check_tie(self.board))

    def test_10_check_tie_false(self):
        self.tile.change_tile(0, "X")
        self.tile.change_tile(1, "O")
        self.tile.change_tile(2, "X")
        self.tile.change_tile(3, "X")
        self.tile.change_tile(4, "O")
        self.tile.change_tile(5, "X")
        self.tile.change_tile(6, "O")
        self.tile.change_tile(7, "O")
        self.tile.change_tile(8, "X")

        self.assertFalse(self.checker.check_tie(self.board))

if __name__ == '__main__':
    unittest.main()
