""" Imports """

from numero import Numero


class ContadorDeLlamadosDecorator(Numero):
    """ Define un contador de llamados para las clases que implementen Número """

    def __init__(self, numero: Numero):
        self._numero = numero
        self._contador = {
            "__str__": 0,
            "__repr__": 0,
            "__eq__": 0,
            "__add__": 0,
            "__sub__": 0,
            "__mul__": 0,
            "__truediv__": 0,
            "__floordiv__": 0,
            "__ge__": 0,
            "__lt__": 0,
        }

    def __str__(self):
        self._contador['__str__'] += 1
        return self._numero.__str__()

    def __repr__(self):
        self._contador['__repr__'] += 1
        return self._numero.__repr__()

    def __eq__(self, otro: Numero) -> bool:
        self._contador['__eq__'] += 1
        return self._numero.__eq__(otro)

    def __add__(self, otro: Numero) -> Numero:
        self._contador['__add__'] += 1
        return self._numero.__add__(otro)

    def __sub__(self, otro: Numero) -> Numero:
        self._contador['__sub__'] += 1
        return self._numero.__sub__(otro)

    def __mul__(self, otro: Numero) -> Numero:
        self._contador['__mul__'] += 1
        return self._numero.__mul__(otro)

    def __truediv__(self, otro: Numero) -> Numero:
        self._contador['__truediv__'] += 1
        return self._numero.__truediv__(otro)

    def __floordiv__(self, otro: Numero) -> Numero:
        self._contador['__floordiv__'] += 1
        return self._numero.__floordiv__(otro)

    def __ge__(self, otro: Numero) -> bool:
        self._contador['__ge__'] += 1
        return self._numero.__ge__(otro)

    def __lt__(self, otro: Numero) -> bool:
        self._contador['__lt__'] += 1
        return self._numero.__lt__(otro)

    def obtener_contador(self, nombre_metodo: str) -> int:
        """ Retorna la cantidad de veces que haya sido utilizado un método """

        return self._contador[nombre_metodo]
