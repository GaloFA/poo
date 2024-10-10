# pylint: skip-file
import os
import tempfile
import unittest

from business.mydatetime import DateTime
from persistence.reservationdao import ReservationDAO

class ReservationDAOTest(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)
        self.dao = ReservationDAO(self.temp_db.name)

        self.room_name = "Sala Test"
        self.start_datetime = DateTime(2024, 9, 24, 20, 10, 15)
        self.end_datetime = DateTime(2024, 9, 24, 21, 10, 15)

        self.start_datetime2 = DateTime(2024, 9, 25, 20, 10, 15)
        self.end_datetime2 = DateTime(2024, 9, 25, 21, 10, 15)

    def tearDown(self):
        self.dao.connection.close()
        self.temp_db.close()
        os.remove(self.temp_db.name)


    def test_01_add_reservation(self):
        self.dao.add_reservation(self.room_name, self.start_datetime, self.end_datetime)
        reservations = self.dao.list_reservations()

        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0][0], self.room_name)
        self.assertEqual(reservations[0][1], str(self.start_datetime))
        self.assertEqual(reservations[0][2], str(self.end_datetime))

    def test_02_remove_reservation(self):
        self.dao.add_reservation(self.room_name, self.start_datetime, self.end_datetime)
        self.dao.remove_reservation(self.room_name, self.start_datetime)
        reservations = self.dao.list_reservations()

        self.assertEqual(len(reservations), 0)

    def test_03_list_multiple_reservations(self):
        self.dao.add_reservation(self.room_name, self.start_datetime, self.end_datetime)
        self.dao.add_reservation(self.room_name, self.start_datetime2, self.end_datetime2)
        reservations = self.dao.list_reservations()

        self.assertEqual(len(reservations), 2)
        self.assertEqual(reservations[0][1], str(self.start_datetime))
        self.assertEqual(reservations[1][1], str(self.start_datetime2))

if __name__ == "__main__":
    unittest.main()
