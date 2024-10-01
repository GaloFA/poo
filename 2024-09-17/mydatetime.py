# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

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


class Date:
    """ Clase que representa una fecha """
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def __eq__(self, other):
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __ge__(self, other):
        return (self._day, self._month, self._year) >= (other._day, other._month, other._year)

    def __lt__(self, other):
        return (self._day, self._month, self._year) < (other._day, other._month, other._year)

    def __str__(self):
        return f"{self._day:02}/{self._month:02}/{self._year}"

class Time:
    """ Clase que representa el tiempo """
    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def __eq__(self, other):
        return (self._hour, self._minute, self._second) == (other._hour, other._minute, other._second)

    def __ge__(self, other):
        return (self._hour, self._minute, self._second) >= (other._hour, other._minute, other._second)

    def __lt__(self, other):
        return (self._hour, self._minute, self._second) < (other._hour, other._minute, other._second)

    def __str__(self):
        return f"{self._hour:02}:{self._minute:02}:{self._second:02}"
