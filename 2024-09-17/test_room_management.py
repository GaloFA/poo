# pylint: skip-file
import unittest
from room import Room
from room_management import RoomManagement

class TestRoomManagement(unittest.TestCase):

    def setUp(self):
        self.room_management = RoomManagement()

    def test_01_añadir_sala(self):
        self.room_management.add_room("Sala 1", 10)
        self.assertEqual(len(self.room_management._rooms), 1)
        self.assertEqual(self.room_management._rooms[0]._name, "Sala 1")
        self.assertEqual(self.room_management._rooms[0]._capacity, 10)

    def test_02_remover_sala(self):
        self.room_management.add_room("Sala 1", 10)
        self.room_management.remove_room("Sala 1", 10)
        self.assertEqual(len(self.room_management._rooms), 0)

    def test_03_remover_sala_inexistente(self):
        with self.assertRaises(ValueError):
            self.room_management.remove_room("Sala 1", 10)

if __name__ == '__main__':
    unittest.main()
