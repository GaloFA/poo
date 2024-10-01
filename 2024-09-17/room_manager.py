# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """

class RoomManager():
    """ Clase que maneja las salas del lugar """
    def __init__(self) -> None:
        self._rooms = []

    def add_room(self, name, capacity):
        """ Método que agrega una sala """
        room = Room(name, capacity)
        self._rooms.append(room)
        return room

    def remove_room(self, name, capacity):
        """ Método que agrega una sala """
        room = Room(name, capacity)
        self._rooms.remove(room)
        return room

    @property
    def rooms(self):
        """ Rooms """
        return self._rooms

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
