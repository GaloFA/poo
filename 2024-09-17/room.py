# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

class Room:
    """ Clase que representa una sala """
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity

    def __str__(self):
        return f"Room {self._name} (Capacity: {self._capacity})"
