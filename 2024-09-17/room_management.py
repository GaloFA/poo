# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from room import Room

class RoomManagement():
    """ Clase que maneja las salas del lugar """
    def __init__(self) -> None:
        self._rooms = []

    def add_room(self, name, capacity):
        """ Método que agrega una sala """
        room = Room(name, capacity)
        self._rooms.append(room)

    def remove_room(self, name, capacity):
        """ Método que agrega una sala """
        room = Room(name, capacity)
        self._rooms.remove(room)
