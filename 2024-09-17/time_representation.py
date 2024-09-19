# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

class Time:
    """ Clase que representa el tiempo """
    def __init__(self, hour, minute):
        self._hour = hour
        self._minute = minute

    def __lt__(self, other):
        return (self._hour, self._minute) < (other.hour, other.minute)

    def __le__(self, other):
        return (self._hour, self._minute) <= (other.hour, other.minute)

    def __eq__(self, other):
        return (self._hour, self._minute) == (other.hour, other.minute)

    def __str__(self):
        return f"{self._hour:02}:{self._minute:02}"
