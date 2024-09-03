# pylint: skip-file
import unittest
from collection_handler import CollectionIterable

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
