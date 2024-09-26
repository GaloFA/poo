# pylint: skip-file
import unittest
from mytime import Time

class TestTime(unittest.TestCase):

    def setUp(self):
        self.time1 = Time(14, 30, 0)
        self.time2 = Time(14, 30, 0)
        self.time3 = Time(10, 15, 30)
        self.time4 = Time(15, 0, 0)
        self.time5 = Time(14, 29, 59)

    def test_01_igual(self):
        self.assertTrue(self.time1 == self.time2)
        self.assertFalse(self.time1 == self.time3)

    def test_02_mayor_o_igual(self):
        self.assertTrue(self.time1 >= self.time2)
        self.assertTrue(self.time1 >= self.time5)
        self.assertFalse(self.time5 >= self.time1)
        self.assertFalse(self.time3 >= self.time1)

    def test_03_menor(self):
        self.assertTrue(self.time5 < self.time1)
        self.assertTrue(self.time3 < self.time1)
        self.assertFalse(self.time1 < self.time3)

    def test_04_string(self):
        self.assertTrue(str(self.time1) == "14:30:00")
        self.assertTrue(str(self.time3) == "10:15:30")

if __name__ == '__main__':
    unittest.main()
