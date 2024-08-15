""" Imports """

from numero import Numero
import fraccion


class Entero(Numero):
    """ Clase Entero """

    def __init__(self, entero: int):
        self.__entero: int = entero

    def __str__(self) -> str:
        return str(self.entero)

    def __repr__(self) -> str:
        return f"Entero({self.entero})"

    def __eq__(self, otro: "Entero") -> bool:
        return self.entero == otro.entero

    def __add__(self, otro: Numero):
        return otro.suma_entero(self) # type: ignore

    def __sub__(self, otro: "Entero") -> "Entero":
        return Entero(self.entero - otro.entero)

    def __mul__(self, otro: Numero) -> Numero:
        return otro.multiplicar_entero(self) # type: ignore

    def __truediv__(self, otro: "Entero"):
        if otro.entero == 0:
            raise ZeroDivisionError("No se puede dividir por cero")

        if self.entero % otro.entero != 0:
            return fraccion.Fraccion(Entero(self.entero), Entero(otro.entero))

        return Entero(self.entero // otro.entero)

    def __floordiv__(self, otro: "Entero") -> "Entero":
        return Entero(self.entero // otro.entero)

    def __ge__(self, otro: "Entero") -> bool:
        return self.entero >= otro.entero

    def __lt__(self, otro: Numero) -> bool:
        return otro._lt_entero(self) # type: ignore

    def suma_entero(self, otro: Numero):
        """ Suma de otro (entero) a un entero"""
        otro = fraccion.Fraccion(otro, self.entero) # type: ignore
        return otro + self

    def _multiplicar_entero(self, otro: Numero):
        """ Multiplicación de otro (entero) a un entero"""
        return Entero(otro.entero * self.entero) # type: ignore

    def _lt_entero(self, otro: Numero) -> bool:
        """ Retornar si el otro es menor que el entero """
        return otro.entero < self.entero # type: ignore

    def _suma_fraccion(self, otro: Numero):
        self_fraccion = fraccion.Fraccion(self, Entero(1))
        return self_fraccion + otro

    def _multiplicar_fraccion(self, otro: Numero):
        self_fraccion = fraccion.Fraccion(self, Entero(1))
        return self_fraccion * otro

    def _lt_fraccion(self, otro: Numero) -> bool:
        num = self * otro.denominador # type: ignore
        return otro.numerador < num  # type: ignore

    @property
    def entero(self):
        """ Property entero """
        return self.__entero
