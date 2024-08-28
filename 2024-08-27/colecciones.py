""" Import """
from collections.abc import Iterable, Iterator

class IteradorDeColeccion(Iterator):
    """ Clase de Iterador """

    def __init__(self, coleccion):
        self._coleccion = coleccion
        self._indice = 0

    def __next__(self):
        if self._indice >= len(self._coleccion):
            raise StopIteration

        resultado = self._coleccion[self._indice]
        self._indice += 1
        return resultado

class ContenedorIterable(Iterable):
    """ Clase de Iterable """

    def __init__(self):
        self._elementos1 = []
        self._elementos2 = []

    def agregar(self, elemento, tipo):
        """ Método que agrega un elemento a la colección """
        if tipo not in (1, 2):
            raise ValueError(f"No existe este tipo: {tipo}")

        if tipo == 1:
            self._elementos1.append(elemento)

        elif tipo == 2:
            self._elementos2.append(elemento)

    def __iter__(self):
        elementos_combinados = self._elementos1 + self._elementos2
        return IteradorDeColeccion(elementos_combinados)

class ContenedorIterable2(Iterable):
    """ Clase de Iterable (usando generaodr) """

    def __init__(self):
        self._elementos1 = []
        self._elementos2 = []

    def agregar(self, elemento, tipo):
        """ Método que agrega un elemento a la colección """
        if tipo not in (1, 2):
            raise ValueError(f"No existe este tipo: {tipo}")

        if tipo == 1:
            self._elementos1.append(elemento)

        elif tipo == 2:
            self._elementos2.append(elemento)

    def __iter__(self):
        for elemento in self._elementos1:
            yield elemento

        for elemento in self._elementos2:
            yield elemento
