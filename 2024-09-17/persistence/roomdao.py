# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import, protected-access, arguments-out-of-order
""" Módulo que contiene el DAO para la Sala """
import sqlite3

class RoomDAO:
    """ Maneja la conexión con la tabla de salas """
    def __init__(self, db_name='reservations.db'):
        self.connection = sqlite3.connect(db_name)
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
        """ Inserta a la tabla las salas """
        with self.connection:
            self.connection.execute('INSERT INTO rooms (name, capacity) VALUES (?, ?)', (name, capacity))

    def list_rooms(self):
        """ Listar salas """
        cursor = self.connection.cursor()
        cursor.execute('SELECT name, capacity FROM rooms')
        return cursor.fetchall()

    def remove_room(self, name):
        """ Remover salas """
        with self.connection:
            self.connection.execute('DELETE FROM rooms WHERE name = ?', (name))
