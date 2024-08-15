""" Imports """

import fraccion as f
from numero import Numero


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

    def __add__(self, otro):
        if isinstance(otro, f.Fraccion):
            num = Entero(int(self.entero) * int(str(otro.denominador)) + int(str(otro.numerador)))
            return f.Fraccion(num, otro.denominador)
        if isinstance(otro, Entero):
            return Entero(self.entero + otro.entero)

    def __sub__(self, otro: "Entero") -> "Entero":
        return Entero(self.entero - otro.entero)

    def __mul__(self, otro):
        if isinstance(otro, f.Fraccion):
            if int(str(self.entero)) % int(str(otro.denominador)) == 0:
                ans = (int(str(self.entero)) * int(str(otro.numerador))) // int(str(otro.denominador))
                return Entero(ans)
            else:
                num = Entero(int(str(self.entero)) * int(str(otro.numerador)))
                return f.Fraccion(num, otro.denominador)
        elif isinstance(otro, Entero):
            return Entero(self.entero * otro.entero)

    def __truediv__(self, otro: "Entero"):
        if otro.entero == 0:
            raise ZeroDivisionError("No se puede dividir por cero")

        if self.entero % otro.entero != 0:
            return f.Fraccion(Entero(self.entero), Entero(otro.entero))

        return Entero(self.entero // otro.entero)

    def __floordiv__(self, otro: "Entero") -> "Entero":
        return Entero(self.entero // otro.entero)

    def __ge__(self, otro: "Entero") -> bool:
        return self.entero >= otro.entero

    def __lt__(self, otro: "Entero") -> bool:
        return self.entero < otro.entero

    def suma_entero(self, otro: Numero):
        """ Suma de otro (entero o fraccion) a un entero"""
        otro = f.Fraccion(otro, self.entero) #type: ignore
        return otro + self

    @property
    def entero(self):
        """ Property entero """
        return self.__entero
