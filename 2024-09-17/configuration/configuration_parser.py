"""Módulo que gestiona la configuración de la aplicación desde un archivo config.json."""

import json
import os

class ConfigurationParser:
    """Clase que carga y gestiona la configuración de la aplicación."""

    DEFAULT_CONFIG_PATH = 'configuration/config.json'

    def __init__(self, config_path=None):
        """Inicializa el parser de configuración.
        
        Args:
            config_path (str): Ruta del archivo de configuración.
            Si no se especifica, se usa 'config.json'.
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self.config = self.__load_configuration()
        self.validate_configuration()

    def __load_configuration(self):
        """ Carga la configuración desde el archivo JSON """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"No se encontró config.json en la ruta: {self.config_path}")

        with open(self.config_path, 'r', encoding='utf-8') as config_file:
            return json.load(config_file)

    def validate_configuration(self):
        """ Valida la configuración cargada para asegurarse de que sea válida """
        backend_type = self.get_backend_type()
        if backend_type not in ['sqlite', 'json']:
            raise ValueError("El tipo de backend es inválido. (sqlite / json)")

    def get_backend_type(self):
        """Obtiene el tipo de backend configurado.
        
        Returns:
            str: El tipo de backend (sqlite o json).
        """
        return self.config.get('backend_type')

    def get_db_path(self):
        """Obtiene la ruta de la base de datos SQLite desde la configuración.
        
        Returns:
            str: La ruta del archivo de base de datos SQLite.
        """
        return self.config.get('db_path')

    def get_reservations_json_path(self):
        """Obtiene la ruta del archivo JSON para las reservas.
        
        Returns:
            str: La ruta del archivo JSON de reservas.
        """
        return self.config.get('reservas_json_path')

    def get_rooms_json_path(self):
        """Obtiene la ruta del archivo JSON para las salas.
        
        Returns:
            str: La ruta del archivo JSON de salas.
        """
        return self.config.get('salas_json_path')
