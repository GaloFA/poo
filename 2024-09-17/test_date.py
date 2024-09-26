# pylint: skip-file
import unittest
from date import Date


class TestDate(unittest.TestCase):

    def setUp(self):
        self.date1 = Date(20, 9, 2024)
        self.date2 = Date(20, 9, 2024)
        self.date3 = Date(9, 6, 2024)

    def test_01_igual(self):
        self.assertTrue(self.date1 == self.date2)
        self.assertFalse(self.date1 == self.date3)

    def test_02_mayor_o_igual(self):
        self.assertTrue(self.date1 >= self.date2)
        self.assertFalse(self.date3 >= self.date1)

    def test_03_menor(self):
        self.assertTrue(self.date3 < self.date1)
        self.assertFalse(self.date1 < self.date3)

    def test_04_string(self):
        self.assertTrue(str(self.date1) == "20/09/2024")
        self.assertTrue(str(self.date3) == "09/06/2024")

if __name__ == '__main__':
    unittest.main()
