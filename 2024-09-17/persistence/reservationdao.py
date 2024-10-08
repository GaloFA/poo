""" Módulo que contiene el DAO para la Reserva """
import sqlite3
from business.mydatetime import DateTime

class ReservationDAO:
    """ Maneja la conexion con la tabla reservas """
    def __init__(self, db_name='reservations.db'):
        # Allow sharing the connection across threads
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
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
