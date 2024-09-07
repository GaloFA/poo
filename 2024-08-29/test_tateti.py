# pylint: skip-file
import unittest
from game import Game

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.game = Game(3)  # 3x3 board
        self.board = self.game._board
        self.players = self.game._players
        self.checker = self.game._checker

    def test_01_match_x_player_wins(self):

        # La partida termina así
        # X | O | X
        # X | O | ▢
        # X | ▢ | O

        # Player X
        self.players[0].place_tile(self.board, 0)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 1)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 2)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 4)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 3)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 8)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 6)

        # Check X wins
        self.assertTrue(self.checker.check_win(self.board))
        self.assertFalse(self.checker.check_tie(self.board))
    
    def test_02_match_o_player_wins(self):

        # La partida termina así
        # X | O | X
        # X | O | ▢
        # ▢ | O | ▢

        # Player X
        self.players[0].place_tile(self.board, 0)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 1)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 3)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 4)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 2)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 7)
        self.players[1].switch_player()

        # Check O wins
        self.assertTrue(self.checker.check_win(self.board))
        self.assertFalse(self.checker.check_tie(self.board))

    def test_03_match_tie(self):

        # La partida termina así
        # X | O | X
        # X | X | O
        # O | X | O

        # Player X
        self.players[0].place_tile(self.board, 0)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 1)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 2)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 5)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 3)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 6)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 4)
        self.players[0].switch_player()

        # Player O
        self.players[1].place_tile(self.board, 8)
        self.players[1].switch_player()

        # Player X
        self.players[0].place_tile(self.board, 7)
        self.players[0].switch_player()

        # Check tie
        self.assertTrue(self.checker.check_tie(self.board))
        self.assertFalse(self.checker.check_win(self.board))

if __name__ == '__main__':
    unittest.main()
