"""Factory para crear DAOs de Reserva según el tipo de backend"""

from persistence.reservation.reservation_sqlite_dao import ReservationSqliteDAO
from persistence.reservation.reservation_json_dao import ReservationJsonDAO

class ReservationDAOFactory:
    """Factory para crear instancias de DAO de Reserva"""

    @staticmethod
    def create_dao(backend_type: str, db_path: str, json_path: str):
        """ Crea una instancia de DAO del backend seleccionado """

        if backend_type == 'sqlite':
            return ReservationSqliteDAO(db_name=db_path if db_path else 'db/reservations.db')
        if backend_type == 'json':
            return ReservationJsonDAO(json_path=json_path)

        raise ValueError(f"Tipo de backend '{backend_type}' no soportado.")
