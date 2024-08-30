# pylint: skip-file
import unittest
from game import Game
from board import Board
from tile import Tile
from player import Player
from checker import Checker

class TestGame(unittest.TestCase):
    
    def test_01_instancia(self):
        game = Game()

        self.assertIsInstance(game, Game)

class TestBoard(unittest.TestCase):

    def test_01_dibjuar_tablero(self):
        board = Board(3)

        drawn_board = board.draw_board()

        self.assertEqual(['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢'], drawn_board)

if __name__ == "__main__":
    unittest.main()