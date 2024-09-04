# pylint: skip-file
import unittest
from collection_handler import CollectionIterable

class TestCollectionIterable(unittest.TestCase):
    def setUp(self):
        self.collection = CollectionIterable()

    def test_01_append_and_getitem(self):
        self.collection.append("A")
        self.collection.append("B")
        self.collection.append("C")
        self.assertEqual(self.collection[0], "A")
        self.assertEqual(self.collection[1], "B")
        self.assertEqual(self.collection[2], "C")

    def test_02_index_out_of_range_error(self):
        with self.assertRaises(IndexError):
            _ = self.collection[0]

    def test_03_check_if_elements_inside_list_are_equal_true(self):
        self.collection.append("X")
        self.collection.append("X")
        self.collection.append("X")

        self.assertTrue(self.collection.check_if_elements_inside_list_are_equal())

    def test_04_check_if_elements_inside_list_are_equal_false(self):
        self.collection.append("X")
        self.collection.append("O")
        self.collection.append("X")

        self.assertFalse(self.collection.check_if_elements_inside_list_are_equal())

    def test_05_iterable(self):
        self.collection.append("X")
        self.collection.append("O")

        iterator = iter(self.collection)
        self.assertEqual(next(iterator), "X")
        self.assertEqual(next(iterator), "O")

    def test_06_stop_iteration(self):
        iterator = iter(self.collection)

        with self.assertRaises(StopIteration):
            next(iterator)

if __name__ == "__main__":
    unittest.main()
