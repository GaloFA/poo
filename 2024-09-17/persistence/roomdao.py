# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import, protected-access, arguments-out-of-order
""" Módulo que contiene el DAO para la Sala """
import sqlite3
import os

class RoomDAO:
    """ Maneja la conexión con la tabla de salas """
    def __init__(self, db_name='db/reservations.db'):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, db_name)
        db_dir = os.path.dirname(db_path)

        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        self.connection = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS rooms (
                    name TEXT PRIMARY KEY,
                    capacity INTEGER
                )
            ''')

    def add_room(self, name, capacity):
        """Inserta a la tabla las salas.
        
        Ejemplo de uso: nueva_sala = self.add_room('Sala B', 20)

        Args:
            name (str): El nombre de la nueva sala.
            capacity (int): La capacidad de la nueva sala.

        Returns:
            None: Este método no devuelve ningún valor. Agrega la sala a la base de datos.
        """
        with self.connection:
            self.connection.execute('INSERT INTO rooms (name, capacity) VALUES (?, ?)', (name, capacity))


    def list_rooms(self):
        """Lista todas las salas disponibles.
        
        Ejemplo de uso: salas = self.list_rooms()

        Returns:
            list: Una lista de tuplas con el nombre y la capacidad de cada sala.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT name, capacity FROM rooms')
        return cursor.fetchall()


    def remove_room(self, name):
        """Remueve una sala del sistema.
        
        Ejemplo de uso: self.remove_room('Sala B')

        Args:
            name (str): El nombre de la sala que se desea eliminar.

        Returns:
            None: Este método no devuelve ningún valor. Elimina la sala de la base de datos.
        """
        with self.connection:
            self.connection.execute('DELETE FROM rooms WHERE name = ?', (name,))
