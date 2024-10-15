"""Interfaz de una clase DAO para salas"""
from abc import ABC, abstractmethod

class RoomDAO(ABC):
    """ Clase abstracta que define los métodos para
    interactuar con la persistencia de datos de salas """

    @abstractmethod
    def add_room(self, name, capacity):
        """Inserta una nueva sala en la base de datos.
        
        Ejemplo de uso: self.add_room('Sala A', 30)

        Args:
            name (str): El nombre de la nueva sala.
            capacity (int): La capacidad de la sala.

        Returns:
            None: No devuelve ningún valor. Agrega la sala a la base de datos.
        """

    @abstractmethod
    def remove_room(self, name):
        """Elimina una sala de la base de datos.
        
        Ejemplo de uso: self.remove_room('Sala A')

        Args:
            name (str): El nombre de la sala que se quiere eliminar.

        Returns:
            None: No devuelve ningún valor. Elimina la sala de la base de datos.
        """

    @abstractmethod
    def list_rooms(self):
        """Lista todas las salas disponibles.
        
        Ejemplo de uso: salas = self.list_rooms()

        Returns:
            list: Una lista de tuplas con el nombre y la capacidad de cada sala.
        """
