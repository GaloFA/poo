# pylint: skip-file
import unittest
from business.mydatetime import DateTime
from business.reservation import Reservation


class TestReservation(unittest.TestCase):

    def setUp(self):
        self.room1 = "Sala 1"
        self.room2 = "Sala 2"
        self.start_time1 = DateTime(20, 9, 2024, 14, 0, 0)
        self.end_time1 = DateTime(20, 9, 2024, 15, 0, 0)
        self.start_time2 = DateTime(20, 9, 2024, 14, 30, 0)
        self.end_time2 = DateTime(20, 9, 2024, 15, 30, 0)
        self.start_time3 = DateTime(20, 9, 2024, 15, 0, 0)
        self.end_time3 = DateTime(20, 9, 2024, 16, 0, 0)
        self.reservation1 = Reservation(
            self.room1, self.start_time1, self.end_time1)
        self.reservation2 = Reservation(
            self.room1, self.start_time2, self.end_time2)
        self.reservation3 = Reservation(
            self.room1, self.start_time3, self.end_time3)
        self.reservation4 = Reservation(
            self.room2, self.start_time1, self.end_time1)

    def test_01_conflicto_con_otra_reserva(self):
        self.assertTrue(self.reservation1.conflicts_with(self.reservation2))

    def test_02_no_hay_conflicto_con_otra_reserva(self):
        self.assertFalse(self.reservation1.conflicts_with(self.reservation3))

    def test_03_no_hay_conflicto_con_otra_reserva_en_otra_sala(self):
        self.assertFalse(self.reservation1.conflicts_with(self.reservation4))

    def test_04_str(self):
        expected_str = f"Reservation in {self.room1} from {
            self.start_time1} to {self.end_time1}"
        self.assertEqual(str(self.reservation1), expected_str)


if __name__ == '__main__':
    unittest.main()
