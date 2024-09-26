# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from date import Date
from mytime import Time

class DateTime:
    """ Clase que representa una fecha y hora """
    def __init__(self, day, month, year, hour, minute, second):
        self._date = Date(day, month, year)
        self._time = Time(hour, minute, second)

    def __eq__(self, other):
        return self._date == other._date and self._time == other._time

    def __ge__(self, other):
        if self._date == other._date:
            return self._time >= other._time
        return self._date >= other._date

    def __lt__(self, other):
        if self._date == other._date:
            return self._time < other._time
        return self._date < other._date

    def __str__(self):
        return f"{self._date} {self._time}"

    @property
    def date(self):
        """ Property date """
        return self._date

    @property
    def time(self):
        """ Property time """
        return self._time
