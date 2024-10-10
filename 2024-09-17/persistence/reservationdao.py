""" Módulo que contiene el DAO para la Reserva """
import sqlite3
import os
from business.mydatetime import DateTime

class ReservationDAO:
    """ Maneja la conexion con la tabla reservas """
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
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    room_name TEXT,
                    start_datetime TEXT,
                    end_datetime TEXT,
                    FOREIGN KEY(room_name) REFERENCES rooms(name)
                )
            ''')

    def list_reservations(self):
        """Lista todas las reservas actuales.
        
        Ejemplo de uso: reservas = self.list_reservations()

        Returns:
            list: Una lista de tuplas con el nombre de la sala, la fecha
            y hora de inicio, y la fecha y hora de fin de cada reserva.
        """
        cursor = self.connection.cursor()
        cursor.execute('SELECT room_name, start_datetime, end_datetime FROM reservations')
        reservations = cursor.fetchall()
        print("Current reservations:", reservations)
        return reservations


    def add_reservation(self, room_name, start_datetime: DateTime, end_datetime: DateTime):
        """Agrega una nueva reserva a la base de datos.
        
        Ejemplo de uso: self.add_reservation('Sala A', inicio, fin)

        Args:
            room_name (str): El nombre de la sala a reservar.
            start_datetime (datetime): La fecha y hora de inicio de la reserva.
            end_datetime (datetime): La fecha y hora de fin de la reserva.

        Returns:
            None: Este método no devuelve ningún valor. Agrega la reserva a la base de datos.
        """
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
        """Elimina una reserva de la base de datos.
        
        Ejemplo de uso: self.remove_reservation('Sala A', inicio)

        Args:
            room_name (str): El nombre de la sala cuya reserva se desea eliminar.
            start_datetime (datetime): La fecha y hora de inicio de la reserva a eliminar.

        Returns:
            None: Este método no devuelve ningún valor. Elimina la reserva de la base de datos.
        """
        with self.connection:
            self.connection.execute('''
                DELETE FROM reservations 
                WHERE room_name = ? AND start_datetime = ?
            ''', (room_name, str(start_datetime)))
