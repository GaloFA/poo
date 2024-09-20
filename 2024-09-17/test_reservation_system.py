import unittest
from reservation import Reservation
from reservation_system import ReservationSystem  # Adjust the import based on your file structure

class TestReservationSystem(unittest.TestCase):

    def setUp(self):
        """Setup a ReservationSystem for testing."""
        self.system = ReservationSystem()
        self.room1 = Reservation('Room 1', '2023-09-19', '10:00', '11:00')
        self.room2 = Reservation('Room 2', '2023-09-19', '12:00', '13:00')
        self.system._rooms.append(self.room1)
        self.system._rooms.append(self.room2)

    def test_make_reservation_success(self):
        """Test successful reservation creation."""
        self.system.make_reservation('Room 1', '2023-09-19', '09:00', '10:00')
        self.assertEqual(len(self.system._reservations), 1)

    def test_make_reservation_room_not_exist(self):
        """Test trying to reserve a non-existent room."""
        with self.assertRaises(ValueError) as context:
            self.system.make_reservation('Room 3', '2023-09-19', '09:00', '10:00')
        self.assertEqual(str(context.exception), 'La sala Room 3 no existe')

    def test_make_reservation_conflict(self):
        """Test trying to reserve a room that's already reserved."""
        self.system.make_reservation('Room 1', '2023-09-19', '09:00', '10:00')
        with self.assertRaises(ValueError) as context:
            self.system.make_reservation('Room 1', '2023-09-19', '09:30', '10:30')
        self.assertEqual(str(context.exception), 'La sala Room 1 ya esta reservada')

    def test_cancel_reservation_success(self):
        """Test successful cancellation of a reservation."""
        self.system.make_reservation('Room 1', '2023-09-19', '09:00', '10:00')
        self.system.cancel_reservation('Room 1', '2023-09-19', '09:00')
        self.assertEqual(len(self.system._reservations), 0)

    def test_cancel_reservation_not_exist(self):
        """Test cancelling a reservation that does not exist."""
        with self.assertRaises(ValueError) as context:
            self.system.cancel_reservation('Room 1', '2023-09-19', '09:00')
        self.assertEqual(str(context.exception), 'No existe la reserva')

    def test_list_reservations(self):
        """Test listing reservations for a specific date."""
        self.system.make_reservation('Room 1', '2023-09-19', '09:00', '10:00')
        self.system.make_reservation('Room 2', '2023-09-19', '12:00', '13:00')
        reservations = self.system.list_reservations('2023-09-19')
        self.assertEqual(len(reservations), 2)

if __name__ == '__main__':
    unittest.main()