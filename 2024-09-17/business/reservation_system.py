# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from business.reservation import Reservation
from business.room_manager import RoomManager
from business.mydatetime import DateTime
from persistence.reservationdao import ReservationDAO

class ReservationSystem:
    """ Clase que representa el sistema de reservas """

    def __init__(self):
        self._room_manager = RoomManager()
        self._reservations = []
        self._reservation_dao = ReservationDAO()
        self.load_reservations()

    def load_reservations(self):
        """ Load reservations from the database into the system """
        reservations_data = self._reservation_dao.list_reservations()
        for room_name, start_datetime_str, end_datetime_str in reservations_data:
            start_date_str, start_time_str = start_datetime_str.split(' ')
            start_day, start_month, start_year = map(int, start_date_str.split('/'))
            start_hour, start_minute, start_second = map(int, start_time_str.split(':'))
            start_datetime = DateTime(start_day, start_month, start_year, start_hour, start_minute, start_second)

            end_date_str, end_time_str = end_datetime_str.split(' ')
            end_day, end_month, end_year = map(int, end_date_str.split('/'))
            end_hour, end_minute, end_second = map(int, end_time_str.split(':'))
            end_datetime = DateTime(end_day, end_month, end_year, end_hour, end_minute, end_second)

            room = next((r for r in self._room_manager.rooms if r.name == room_name), None)
            if room:
                self._reservations.append(Reservation(room, start_datetime, end_datetime))


    def make_reservation(self, room_name, start_datetime, end_datetime):
        """ Método que hace una reserva """
        room = next(
            (r for r in self._room_manager.rooms if r.name == room_name), None)
        if not room:
            raise ValueError(f"La sala {room_name} no existe")

        new_reservation = Reservation(room, start_datetime, end_datetime)

        for reservation in self._reservations:
            if new_reservation.conflicts_with(reservation):
                raise ValueError(f"La sala {room_name} ya está reservada")

        self._reservations.append(new_reservation)
        self._reservation_dao.add_reservation(room_name, start_datetime, end_datetime)

    def cancel_reservation(self, room_name, start_datetime: "DateTime"):
        """ Método que cancela una reserva """
        for reservation in self._reservations:
            if reservation.room.name == room_name and reservation.start_datetime == start_datetime:
                self._reservations.remove(reservation)
                self._reservation_dao.remove_reservation(room_name, start_datetime)
                return
        raise ValueError("No existe la reserva")

    def list_reservations(self, date):
        """ Método que retorna una lista de las reservas activas en un determinado día """
        reservation_list = []
        for reservation in self._reservations:
            if reservation.start_datetime.date == date:
                reservation_list.append(reservation)

        return reservation_list

    def list_all_reservations(self):
        """ Método que retorna una lista de todas las reservas activas """
        return self._reservations

    @property
    def reservations(self):
        """ Reservations """
        return self._reservations
