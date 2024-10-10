# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Módulo que contiene las salas y maneras de manejarlas (agregar o borrar) """
from persistence.roomdao import RoomDAO

class RoomManager:
    """ Clase que maneja las salas del lugar """
    def __init__(self) -> None:
        self._rooms = []
        self._room_dao = RoomDAO()
        self._load_rooms()

    def _load_rooms(self):
        rooms_data = self._room_dao.list_rooms()
        self._rooms = [Room(name, capacity) for name, capacity in rooms_data]

    def add_room(self, name, capacity):
        """Agrega una nueva sala al sistema.
    
        Ejemplo de uso: nueva_sala = self.add_room('Sala B', 20)

        Args:
            name (str): El nombre de la nueva sala.
            capacity (int): La capacidad de la nueva sala.

        Returns:
            Room: La sala recién creada.
        """
        room = Room(name, capacity)
        self._room_dao.add_room(name, capacity)
        self._rooms.append(room)
        return room

    def remove_room(self, name):
        """Elimina una sala del sistema.
    
        Ejemplo de uso: self.remove_room('Sala B')

        Args:
            name (str): El nombre de la sala que se desea eliminar.

        Returns:
            None: Este método no devuelve ningún valor. Elimina la sala de la lista interna de salas.
        """
        self._room_dao.remove_room(name)
        self._rooms = [room for room in self._rooms if room.name != name]

    def list_rooms(self):
        """ Método que muestra salas """
        return self._rooms

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

    @property
    def capacity(self):
        """ Property capacity """
        return self._capacity
