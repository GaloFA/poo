# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

class Date:
    """ Clase que representa una fecha """
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    def __eq__(self, other):
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __str__(self):
        return f"{self._day:02}/{self._month:02}/{self._year}"
