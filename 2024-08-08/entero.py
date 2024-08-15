""" Imports """
# pylint: disable=protected-access

from numero import Numero
import fraccion

class Entero(Numero):
    """ Clase Entero """

    def __init__(self, entero: int):
        self.__entero: int = entero

    def __str__(self) -> str:
        return str(self.__entero)

    def __repr__(self) -> str:
        return f"Entero({self.__entero})"

    def __eq__(self, otro: "Entero") -> bool:
        return self.__entero == otro.__entero

    def __add__(self, otro: Numero):
        return otro.suma_entero(self) # type: ignore

    def __sub__(self, otro: "Entero") -> "Entero":
        return Entero(self.__entero - otro.__entero)

    def __mul__(self, otro: Numero) -> Numero:
        return otro.multiplicar_entero(self) # type: ignore

    def __truediv__(self, otro: "Entero"):
        if otro.__entero == 0:
            raise ZeroDivisionError("No se puede dividir por cero")

        if self.__entero % otro.__entero != 0:
            return fraccion.Fraccion(Entero(self.__entero), Entero(otro.__entero))

        return Entero(self.__entero // otro.__entero)

    def __floordiv__(self, otro: "Entero") -> "Entero":
        return Entero(self.__entero // otro.__entero)

    def __ge__(self, otro: "Entero") -> bool:
        return self.__entero >= otro.__entero

    def __lt__(self, otro: Numero) -> bool:
        return otro._lt_entero(self) # type: ignore

    def suma_entero(self, otro: Numero):
        """ Suma de otro (entero) a un entero"""
        otro = fraccion.Fraccion(otro, self.__entero) # type: ignore
        return otro + self

    def multiplicar_entero(self, otro: Numero):
        """ Multiplicación de otro (entero) a un entero"""
        return Entero(otro.__entero * self.__entero) # type: ignore

    def lt_entero(self, otro: Numero) -> bool:
        """ Retornar si el otro (entero) es menor que el entero """
        return otro.__entero < self.__entero # type: ignore

    def suma_fraccion(self, otro: Numero):
        """ Suma de otro (fracción) a un entero"""
        self_fraccion = fraccion.Fraccion(self, Entero(1))
        return self_fraccion + otro

    def multiplicar_fraccion(self, otro: Numero):
        """ Multiplicación de otro (fracción) a un entero"""
        self_fraccion = fraccion.Fraccion(self, Entero(1))
        return self_fraccion * otro

    def lt_fraccion(self, otro: Numero) -> bool:
        """ Retornar si el otro (fracción) es menor que el entero """
        num = self * otro.__denominador # type: ignore
        return otro.__numerador < num  # type: ignore

    @property
    def entero(self):
        """ Property entero """
        return self.__entero
