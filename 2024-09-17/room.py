# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

class Room:
    """ Clase que representa una sala """
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity

    def __eq__(self, other):
        return self._name == other._name and self._capacity == other._capacity

    @property
    def name(self):
        """ Property name """
        return self._name
