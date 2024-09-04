# pylint: skip-file
import unittest
from board import Board
from board_render import BoardRender

class TestBoardRender(unittest.TestCase):

    def setUp(self):
        """ Configuración que se ejecuta antes de cada prueba """
        self.board = Board(3)
        self.board_render = BoardRender(self.board)

    def test_01_board_draw(self):
        expected_output = "▢   ▢   ▢   \n▢   ▢   ▢   \n▢   ▢   ▢   \n"
        self.assertEqual(self.board_render.draw_board(), expected_output)

    def test_02_board_draw_dimensions_5(self):
        board = Board(5)
        board_render = BoardRender(board)

        expected_output = "▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n"
        self.assertEqual(board_render.draw_board(), expected_output)

if __name__ == "__main__":
    unittest.main()
