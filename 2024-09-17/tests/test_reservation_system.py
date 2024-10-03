# pylint: skip-file
import unittest
from business.reservation_system import ReservationSystem
from business.mydatetime import DateTime


class TestReservationSystem(unittest.TestCase):

    def setUp(self):
        self.system = ReservationSystem()

        self.system._room_manager.add_room("Sala 1", 10)
        self.system._room_manager.add_room("Sala 2", 20)

        self.start_datetime = DateTime(20, 9, 2024, 14, 0, 0)
        self.end_datetime = DateTime(20, 9, 2024, 15, 0, 0)

    def test_01_hacer_reserva(self):
        self.system.make_reservation(
            "Sala 1", self.start_datetime, self.end_datetime)
        self.assertEqual(len(self.system._reservations), 1)

    def test_02_hacer_reserva_con_conflicto(self):
        self.system.make_reservation(
            "Sala 1", self.start_datetime, self.end_datetime)
        with self.assertRaises(ValueError):
            overlapping_start = DateTime(20, 9, 2024, 14, 30, 0)
            overlapping_end = DateTime(20, 9, 2024, 15, 30, 0)
            self.system.make_reservation(
                "Sala 1", overlapping_start, overlapping_end)

    def test_03_cancelar_reserva(self):
        self.system.make_reservation(
            "Sala 1", self.start_datetime, self.end_datetime)
        self.system.cancel_reservation("Sala 1", self.start_datetime)
        self.assertEqual(len(self.system._reservations), 0)

    def test_04_cancelar_reserva_no_existente(self):
        with self.assertRaises(ValueError):
            self.system.cancel_reservation("Sala 1", self.start_datetime)

    def test_05_listar_reservas(self):
        self.system.make_reservation(
            "Sala 1", self.start_datetime, self.end_datetime)
        reservations = self.system.list_reservations(self.start_datetime.date)
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0]._room.name, "Sala 1")


if __name__ == '__main__':
    unittest.main()
