# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from reservation import Reservation

class ReservationSystem:
    """ Clase que representa el sistema de reservas """
    def __init__(self):
        self._rooms = []
        self._reservations = []

    def make_reservation(self, room_name, date, start_time, end_time):
        """ Método que hace una reserva """
        room = next((r for r in self._rooms if r.name == room_name), None)
        if not room:
            raise ValueError(f"La sala {room_name} no existe")

        new_reservation = Reservation(room, date, start_time, end_time)

        for reservation in self._reservations:
            if new_reservation.conflicts_with(reservation):
                raise ValueError(f"La sala {room_name} ya esta reservada")

        self._reservations.append(new_reservation)

    def cancel_reservation(self, room_name, date, start_time):
        """ Método que cancela una reserva """
        for reservation in self._reservations:
            if reservation.room.name == room_name and reservation.date == date and reservation.start_time == start_time:
                self._reservations.remove(reservation)
                return
        raise ValueError("No existe la reserva")

    def list_reservations(self, date):
        """ Método que retorna una lista de las reservas activas en un determinado día """
        reservation_list = []
        for element in self._reservations:
            if element.date == date:
                reservation_list.append(element)

        return reservation_list
