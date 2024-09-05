# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods
""" Imports """
from collections.abc import Iterable, Iterator

class CollectionIterator(Iterator):
    """ Clase de iterador """

    def __init__(self, collection: list):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index >= len(self._collection):
            raise StopIteration

        result = self._collection[self._index]
        self._index += 1
        return result

class CollectionIterable(Iterable):
    """ Clase que maneja las colecciones de todo el programa """

    def __init__(self):
        self._elements = []

    def __iter__(self):
        return iter(self._elements)

    def __getitem__(self, index):
        if not (0 <= index < len(self._elements)):
            raise IndexError("Index out of range")

        return self._elements[index]

    def __setitem__(self, index: int, value: str):
        if not (0 <= index < len(self._elements)):
            raise IndexError("Index out of range")

        self._elements[index] = value

    def append(self, value: str):
        """ Método que permite agregar elementos a la lista que se está manejando """

        self._elements.append(value)

    def check_if_elements_inside_list_are_equal(self) -> bool:
        """ Método que verifica si los elementos dentro de una lista son iguales """

        element = self._elements[0]

        for item in self._elements:
            if element != item:
                return False

            if item == "▢":
                return False

        return True

    @property
    def get_list(self):
        """ Retorna la lista """

        return self._elements
