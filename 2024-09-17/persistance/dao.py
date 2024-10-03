# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, unused-import, protected-access, arguments-out-of-order
""" Módulo que hace la conexión de la base de datos con la capa de negocio """
import sqlite3
from business.mydatetime import DateTime

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
            self.connection.execute('DELETE FROM rooms WHERE name = ?', (name,))

class ReservationDAO:
    """ Maneja la conexion con la tabla reservas """
    def __init__(self, db_name='reservations.db'):
        self.connection = sqlite3.connect(db_name)
        self._create_table()

    def _create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_name TEXT,
                    start_datetime TEXT,
                    end_datetime TEXT,
                    FOREIGN KEY(room_name) REFERENCES rooms(name)
                )
            ''')

    def add_reservation(self, room_name, start_datetime: DateTime, end_datetime: DateTime):
        """ Agregar reserva """
        with self.connection:
            self.connection.execute('''
                INSERT INTO reservations (room_name, start_datetime, end_datetime)
                VALUES (?, ?, ?)
            ''', (room_name, str(start_datetime), str(end_datetime)))

    def list_reservations(self):
        """ Listar reservas """
        cursor = self.connection.cursor()
        cursor.execute('SELECT room_name, start_datetime, end_datetime FROM reservations')
        return cursor.fetchall()

    def remove_reservation(self, room_name, start_datetime: DateTime):
        """ Remover reserva """
        with self.connection:
            self.connection.execute('''
                DELETE FROM reservations 
                WHERE room_name = ? AND start_datetime = ?
            ''', (room_name, str(start_datetime)))
