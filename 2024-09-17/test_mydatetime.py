# pylint: skip-file
import unittest
from mydatetime import DateTime

class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.datetime1 = DateTime(20, 9, 2024, 14, 30, 0)
        self.datetime2 = DateTime(20, 9, 2024, 14, 30, 0)
        self.datetime3 = DateTime(9, 6, 2024, 10, 0, 0)
        self.datetime4 = DateTime(20, 9, 2024, 15, 0, 0)
        self.datetime5 = DateTime(20, 9, 2024, 14, 29, 0)

    def test_01_igual(self):
        self.assertTrue(self.datetime1 == self.datetime2)
        self.assertFalse(self.datetime1 == self.datetime3)

    def test_02_mayor_o_igual(self):
        self.assertTrue(self.datetime1 >= self.datetime2)
        self.assertTrue(self.datetime1 >= self.datetime5)
        self.assertFalse(self.datetime5 >= self.datetime1)
        self.assertFalse(self.datetime3 >= self.datetime1)

    def test_03_menor(self):
        self.assertTrue(self.datetime5 < self.datetime1)
        self.assertTrue(self.datetime3 < self.datetime1)
        self.assertFalse(self.datetime1 < self.datetime3)

    def test_04_string(self):
        self.assertTrue(str(self.datetime1) == "20/09/2024 14:30:00")
        self.assertTrue(str(self.datetime3) == "09/06/2024 10:00:00")

if __name__ == '__main__':
    unittest.main()
