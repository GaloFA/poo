# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

class Reservation:
    """ Clase que representa una reserva de una sala """
    def __init__(self, room, date, start_time, end_time):
        self._room = room
        self._date = date
        self._start_time = start_time
        self._end_time = end_time

    def conflicts_with(self, other_reservation):
        """ Método que verifica que no exista otra reserva en la misma sala, en el mismo momento """
        if self._date == other_reservation.date and self._room == other_reservation.room:
            return not (self._end_time <= other_reservation.start_time or self._start_time >= other_reservation.end_time)
        return False

    def __str__(self):
        return f"Reservation in {self._room} on {self._date} from {self._start_time} to {self._end_time}"

    @property
    def start_time(self):
        """ start time """
        return self.start_time

    @property
    def end_time(self):
        """ start time """
        return self.start_time
