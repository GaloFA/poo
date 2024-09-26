# pylint: skip-file
import unittest
from room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room("Sala 1", 10)
        self.room2 = Room("Sala 2", 20)
        self.room3 = Room("Sala 1", 10)

    def test_01_sala_igual(self):
        self.assertEqual(self.room1, self.room3)

    def test_02_sala_distinta(self):
        self.assertNotEqual(self.room1, self.room2)

if __name__ == '__main__':
    unittest.main()
