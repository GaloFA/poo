""" Imports """
# pylint: disable=protected-access, line-too-long

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
        return self.__entero == otro # type: ignore

    def __add__(self, otro: Numero):
        return otro.suma_entero(self)  # type: ignore

    def __sub__(self, otro: "Entero") -> "Entero":
        return Entero(self.__entero - otro._Entero__entero) # type: ignore

    def __mul__(self, otro: Numero) -> Numero:
        return otro.multiplicar_entero(self)  # type: ignore

    def __truediv__(self, otro: "Entero"):
        if otro._Entero__entero == 0: # type: ignore
            raise ZeroDivisionError("No se puede dividir por cero")

        if self.__entero % otro._Entero__entero != 0: # type: ignore
            fraccion_final = fraccion.Fraccion(Entero(self.__entero), Entero(otro._Entero__entero)) # type: ignore
            return fraccion_final

        return Entero(self.__entero // otro._Entero__entero) # type: ignore

    def __floordiv__(self, otro: "Entero") -> "Entero":
        return Entero(self.__entero // otro._Entero__entero) # type: ignore

    def __ge__(self, otro: "Entero") -> bool:
        return self.__entero >= otro._Entero__entero # type: ignore

    def __lt__(self, otro: Numero) -> bool:
        return otro.lt_entero(self)  # type: ignore

    def suma_entero(self, otro):
        """ Suma de otro (entero) a un entero"""
        return Entero(otro.__entero + self.__entero)

    def suma_fraccion(self, otro):
        """ Suma de otro (fracción) a un entero"""
        self_fraccion = fraccion.Fraccion(self, Entero(1))
        numerador_final = self_fraccion._Fraccion__numerador * otro._Fraccion__denominador + self_fraccion._Fraccion__denominador * otro._Fraccion__numerador # type: ignore
        denominador_final = self_fraccion._Fraccion__denominador * otro._Fraccion__denominador # type: ignore
        return fraccion.Fraccion(numerador_final, denominador_final)

    def multiplicar_entero(self, otro: Numero):
        """ Multiplicación de otro (entero) a un entero"""
        return Entero(otro._Entero__entero * self.__entero)  # type: ignore

    def multiplicar_fraccion(self, otro):
        """ Multiplicación de otro (fracción) a un entero"""
        if self.__entero % otro._Fraccion__denominador.entero == 0:
            return otro.numerador
        else:
            self_fraccion = fraccion.Fraccion(self, Entero(1))
            numerador_final = otro._Fraccion__numerador * self_fraccion._Fraccion__numerador # type: ignore
            denominador_final = otro._Fraccion__denominador * self_fraccion._Fraccion__denominador # type: ignore
            return fraccion.Fraccion(numerador_final, denominador_final)

    def lt_entero(self, otro: Numero) -> bool:
        """ Retornar si el otro (entero) es menor que el entero """
        return otro._Entero__entero < self.__entero  # type: ignore

    def lt_fraccion(self, otro: Numero) -> bool:
        """ Retornar si el otro (fracción) es menor que el entero """
        return self.__entero < (otro._Fraccion__numerador.entero/otro._Fraccion__denominador.entero)  # type: ignore
