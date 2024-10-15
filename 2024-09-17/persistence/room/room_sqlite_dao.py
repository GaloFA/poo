# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import, protected-access, arguments-out-of-order
""" Módulo que contiene el DAO para la Sala """
import sqlite3
import os
from persistence.room.roomdao import RoomDAO

class RoomSqliteDAO(RoomDAO):
    """ Maneja la conexión con la tabla de salas """
    def __init__(self, db_name='data/db/reservation.db'):
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

        with self.connection:
            self.connection.execute('INSERT INTO rooms (name, capacity) VALUES (?, ?)', (name, capacity))

    def remove_room(self, name):

        with self.connection:
            self.connection.execute('DELETE FROM rooms WHERE name = ?', (name,))

    def list_rooms(self):

        cursor = self.connection.cursor()
        cursor.execute('SELECT name, capacity FROM rooms')
        return cursor.fetchall()
