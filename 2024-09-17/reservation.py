# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from mydatetime import DateTime

class Reservation:
    """ Clase que representa una reserva de una sala """
    def __init__(self, room, start_datetime: "DateTime", end_datetime: "DateTime"):
        self._room = room
        self._start_datetime = start_datetime
        self._end_datetime = end_datetime

    def conflicts_with(self, other_reservation):
        """ Método que verifica que no exista otra reserva en la misma sala, en el mismo momento """
        if self._room == other_reservation.room:
            return not (self._end_datetime <= other_reservation.start_datetime or self._start_datetime >= other_reservation.end_datetime)
        return False

    def __str__(self):
        return f"Reservation in {self._room} from {self._start_datetime} to {self._end_datetime}"

    @property
    def start_datetime(self):
        """ Start time """
        return self._start_datetime

    @property
    def end_datetime(self):
        """ End time """
        return self._end_datetime

    @property
    def room(self):
        """ Room """
        return self._room
