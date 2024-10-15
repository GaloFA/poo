""" Módulo que contiene el DAO para la Reserva """
import sqlite3
import os
from business.mydatetime import DateTime
from persistence.reservation.reservationdao import ReservationDAO

class ReservationSqliteDAO(ReservationDAO):
    """ Maneja la conexion con la tabla reservas """
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
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_name TEXT,
                    start_datetime TEXT,
                    end_datetime TEXT,
                    FOREIGN KEY(room_name) REFERENCES rooms(name)
                )
            ''')

    def add_reservation(self, room_name, start_datetime: DateTime, end_datetime: DateTime):

        print(f"Room: {room_name}, Start: {start_datetime}, End: {end_datetime}")
        try:
            with self.connection:
                self.connection.execute('''
                    INSERT INTO reservations (room_name, start_datetime, end_datetime)
                    VALUES (?, ?, ?)
                ''', (room_name, str(start_datetime), str(end_datetime)))
            print("Reservation added successfully.")
        except ValueError as e:
            print(f"Error adding reservation: {e}")

    def remove_reservation(self, room_name, start_datetime: DateTime):

        with self.connection:
            self.connection.execute('''
                DELETE FROM reservations 
                WHERE room_name = ? AND start_datetime = ?
            ''', (room_name, str(start_datetime)))

    def list_reservations(self):

        cursor = self.connection.cursor()
        cursor.execute('SELECT room_name, start_datetime, end_datetime FROM reservations')
        reservations = cursor.fetchall()
        print("Current reservations:", reservations)
        return reservations
