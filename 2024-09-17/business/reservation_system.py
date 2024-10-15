# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Módulo que contiene un sistema de reservas, pudiendo hacerlas, cancelarlas o listarlas. """
from business.reservation import Reservation
from business.room_manager import RoomManager
from business.mydatetime import DateTime
from persistence.reservation.reservation_factory_dao import ReservationDAOFactory
from configuration.configuration_parser import ConfigurationParser

class ReservationSystem:
    """ Clase que representa el sistema de reservas """

    def __init__(self, config: ConfigurationParser):
        self._room_manager = RoomManager()
        self._reservations = []
        self._reservation_dao = ReservationDAOFactory.create_dao(config.get_backend_type(), config.get_db_path(), config.get_reservas_json_path())
        self.load_reservations()

    def load_reservations(self):
        """Carga reservas desde la base de datos.
    
        Ejemplo de uso: self.load_reservations()

        Returns:
            None: Este método no devuelve ningún valor. Carga las reservas en la lista interna de reservas.
        """
        reservations = self._reservation_dao.list_reservations()
        for room_name, start_datetime, end_datetime in reservations:
            print(f"Loaded reservation: {room_name}, {start_datetime} to {end_datetime}")
            self._reservations.append(Reservation(room_name, start_datetime, end_datetime))

    def make_reservation(self, room_name: str, start_datetime: DateTime, end_datetime: DateTime):
        """Realiza una reserva para una sala especificada.

        Ejemplo de uso: self.make_reservation('Sala A', inicio, fin)

        Args:
            room_name (str): El nombre de la sala a reservar.
            start_datetime (DateTime): La fecha y hora de inicio de la reserva.
            end_datetime (DateTime): La fecha y hora de fin de la reserva.

        Raises:
            ValueError: Si la sala no existe o si la reserva entra en conflicto con una reserva existente.

        Returns:
            None: Este método no devuelve ningún valor. Agrega la reserva a la lista interna de reservas.
        """
        room = next((r for r in self._room_manager.rooms if r.name == room_name), None)
        if not room:
            raise ValueError(f"La sala {room_name} no existe")

        new_reservation = Reservation(room, start_datetime, end_datetime)

        for reservation in self._reservations:
            if new_reservation.conflicts_with(reservation):
                raise ValueError(f"La sala {room_name} ya está reservada")

        self._reservations.append(new_reservation)
        self._reservation_dao.add_reservation(room_name, start_datetime, end_datetime)

    def cancel_reservation(self, room_name: str, start_datetime: DateTime):
        """Cancela una reserva existente para una sala específica.
    
        Ejemplo de uso: self.cancel_reservation('Sala A', inicio)

        Args:
            room_name (str): El nombre de la sala cuya reserva se desea cancelar.
            start_datetime (DateTime): La fecha y hora de inicio de la reserva a cancelar.

        Raises:
            ValueError: Si no existe una reserva coincidente para la sala y el inicio especificados.

        Returns:
            None: Este método no devuelve ningún valor. Elimina la reserva de la lista interna de reservas.
        """
        for reservation in self._reservations:
            if reservation.room.name == room_name and reservation.start_datetime == start_datetime:
                self._reservations.remove(reservation)
                self._reservation_dao.remove_reservation(room_name, start_datetime)
                return
        raise ValueError("No existe la reserva")

    def list_reservations(self, date: DateTime):
        """Retorna una lista de las reservas activas en un día específico.
    
        Ejemplo de uso: reservas = self.list_reservations(fecha)

        Args:
            date (Date): La fecha para la cual se desean listar las reservas.

        Returns:
            list: Una lista de reservas activas en la fecha especificada.
        """
        reservation_list = []
        for reservation in self._reservations:
            if reservation.start_datetime.date == date.date:
                reservation_list.append(reservation)

        return reservation_list

    def list_all_reservations(self):
        """ Método que retorna una lista de todas las reservas activas """
        return self._reservations

    @property
    def reservations(self):
        """ Reservations """
        return self._reservations
