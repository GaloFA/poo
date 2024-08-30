# pylint: skip-file
import unittest
from game import Game
from board import Board
from tile import Tile
from player import Player
from checker import Checker

class TestJuego(unittest.TestCase):
    
    def test_01_instancia(self):
        game = Game()

        self.assertIsInstance(game, Game)

if __name__ == "__main__":
    unittest.main()