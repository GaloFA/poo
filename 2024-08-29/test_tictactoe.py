# pylint: skip-file
import unittest
from game import Game
from board import Board
from tile import Tile, InvalidPositionValueError, InvalidTileTypeError
from player import Player
from checker import Checker
from collection_handler import CollectionIterable


class TestBoard(unittest.TestCase):

    def test_01_board_length(self):
        board = Board(3)

        board_list = board.get_board_list()

        self.assertEqual(len(board_list), 9)

    def test_02_board_drawn(self):
        board = Board(3)

        board_list = board.get_board_list()

        for cell in board_list:
            self.assertEqual(cell, "▢")

    def test_03_board_get_item(self):
        board = Board(3)

        element = board[0]

        self.assertEqual(element, "▢")

    def test_04_board_index_out_of_range_error(self):
        board = Board(3)

        with self.assertRaises(IndexError):
            _ = board[9]

    def test_05_board_draw(self):
        board = Board(3)

        expected_output = "▢   ▢   ▢   \n▢   ▢   ▢   \n▢   ▢   ▢   \n"

        self.assertEqual(board.draw_board(), expected_output)

    def test_06_board_draw_dimensions_5(self):
        board = Board(5)

        expected_output = "▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n▢   ▢   ▢   ▢   ▢   \n"

        self.assertEqual(board.draw_board(), expected_output)


class TestTile(unittest.TestCase):

    def test_01_change_tile_valid_position(self):
        board = Board(3)
        tile = Tile(board, 0)

        tile.change_tile(0, "X")

        self.assertEqual(board.get_board_list()[0], "X")

    def test_02_change_tile_invalid_position(self):
        board = Board(3)
        tile = Tile(board, 0)

        with self.assertRaises(InvalidPositionValueError):
            tile.change_tile(9, "X")

        with self.assertRaises(InvalidPositionValueError):
            tile.change_tile(-1, "X")

    def test_03_change_tile_invalid_type(self):
        board = Board(3)
        tile = Tile(board, 0)

        with self.assertRaises(InvalidTileTypeError):
            tile.change_tile(0, "A")

        with self.assertRaises(InvalidTileTypeError):
            tile.change_tile(0, "")


class TestCollectionIterable(unittest.TestCase):
    def test_01_append_and_getitem(self):
        collection = CollectionIterable()

        collection.append("A")
        collection.append("B")
        collection.append("C")
        self.assertEqual(collection[0], "A")
        self.assertEqual(collection[1], "B")
        self.assertEqual(collection[2], "C")

    def test_02_index_out_of_range_error(self):
        collection = CollectionIterable()

        with self.assertRaises(IndexError):
            _ = collection[0]

    def test_03_check_if_elements_inside_list_are_equal_true(self):
        collection = CollectionIterable()

        collection.append("X")
        collection.append("X")
        collection.append("X")

        self.assertTrue(collection.check_if_elements_inside_list_are_equal())

    def test_04_check_if_elements_inside_list_are_equal_false(self):
        collection = CollectionIterable()

        collection.append("X")
        collection.append("O")
        collection.append("X")

        self.assertFalse(collection.check_if_elements_inside_list_are_equal())

    def test_05_iterable(self):
        collection = CollectionIterable()

        collection.append("X")
        collection.append("O")

        iterator = iter(collection)
        self.assertEqual(next(iterator), "X")
        self.assertEqual(next(iterator), "O")


    def test_06_stop_iteration(self):
        collection = CollectionIterable()

        iterator = iter(collection)

        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    unittest.main()
