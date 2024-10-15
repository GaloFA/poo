"""Factory para crear DAOs de Sala según el tipo de backend"""

from persistence.room.room_sqlite_dao import RoomSqliteDAO
from persistence.room.room_json_dao import RoomJsonDAO

class RoomDAOFactory:
    """Factory para crear instancias de DAO de Sala"""

    @staticmethod
    def create_dao(backend_type: str, db_path: str, json_path: str):
        """ Crea una instancia de DAO del backend seleccionado """

        if backend_type == 'sqlite':
            return RoomSqliteDAO(db_name=db_path if db_path else 'db/reservations.db')
        if backend_type == 'json':
            return RoomJsonDAO(json_path=json_path)

        raise ValueError(f"Tipo de backend '{backend_type}' no soportado.")
