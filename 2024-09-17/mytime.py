# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

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
