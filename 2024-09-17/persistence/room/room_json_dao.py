# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, invalid-name
""" Módulo que contiene el DAO para la Sala usando JSON """
import json
import os
from persistence.room.roomdao import RoomDAO

class RoomJsonDAO(RoomDAO):
    """ Maneja la conexión con el archivo JSON para salas """
    def __init__(self, json_path='data/json/rooms.json'):
        self.json_path = json_path
        self._initialize_file()

    def _initialize_file(self):
        if not os.path.exists(self.json_path):
            with open(self.json_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_room(self, name, capacity):

        room = {
            'name': name,
            'capacity': capacity
        }
        rooms = self.list_rooms()
        rooms.append(room)

        with open(self.json_path, 'w', encoding='utf-8') as file:
            json.dump(rooms, file)

    def remove_room(self, name):

        rooms = self.list_rooms()
        rooms = [room for room in rooms if room['name'] != name]

        with open(self.json_path, 'w', encoding='utf-8') as file:
            json.dump(rooms, file)

    def list_rooms(self):

        with open(self.json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
