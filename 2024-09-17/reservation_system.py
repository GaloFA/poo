# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from reservation import Reservation
from room_management import RoomManagement

class ReservationSystem:
    """ Clase que representa el sistema de reservas """
    def __init__(self):
        self._room_management = RoomManagement()
        self._reservations = []

    def make_reservation(self, room_name, start_datetime, end_datetime):
        """ Método que hace una reserva """
        room = next((r for r in self._room_management.rooms if r.name == room_name), None)
        if not room:
            raise ValueError(f"La sala {room_name} no existe")

        new_reservation = Reservation(room, start_datetime, end_datetime)

        for reservation in self._reservations:
            if new_reservation.conflicts_with(reservation):
                raise ValueError(f"La sala {room_name} ya esta reservada")

        self._reservations.append(new_reservation)

    def cancel_reservation(self, room_name, start_datetime):
        """ Método que cancela una reserva """
        for reservation in self._reservations:
            if reservation.room.name == room_name and reservation.start_datetime == start_datetime:
                self._reservations.remove(reservation)
                return
        raise ValueError("No existe la reserva")

    def list_reservations(self, date):
        """ Método que retorna una lista de las reservas activas en un determinado día """
        reservation_list = []
        for reservation in self._reservations:
            # Ensure reservation's date and the input date are both Date objects for comparison
            if reservation.start_datetime.date == date:
                reservation_list.append(reservation)

        return reservation_list


    @property
    def reservations(self):
        """ Reservations """
        return self._reservations
