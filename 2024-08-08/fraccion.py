"""Import classes"""
# pylint: disable=protected-access

from numero import Numero
import entero

class Fraccion(Numero):
    """ Clase Fraccion """
    def __init__(self, numerador: entero.Entero, denominador: entero.Entero):
        if not isinstance(numerador, entero.Entero):
            raise ValueError("El numerador debe ser de tipo Entero")

        if not isinstance(denominador, entero.Entero):
            raise ValueError("El denominador debe ser de tipo Entero")

        if denominador == entero.Entero(0):
            raise ZeroDivisionError("El denominador no puede ser cero")

        self.__numerador: entero.Entero = numerador
        self.__denominador: entero.Entero = denominador

    def __str__(self) -> str:
        return f"{self.__numerador}/{self.__denominador}"

    def __repr__(self) -> str:
        return f"Fraccion({self.__numerador}/{self.__denominador})"

    def __eq__(self, otro: "Fraccion") -> bool:
        return self.__numerador == otro.__numerador and self.__denominador == otro.__denominador

    def __add__(self, otro: Numero):
        return otro.suma_fraccion(self) # type: ignore

    def __sub__(self, otro: "Fraccion") -> "Fraccion":
        if self.__denominador != otro.__denominador:
            raise NotImplementedError("No está implementada la resta con denominadores distintos")

        temp_numerador = self.__numerador - otro.__numerador
        return Fraccion(temp_numerador, self.__denominador)

    def __mul__(self, otro: Numero):
        return otro.multiplicar_fraccion(self) # type: ignore

    def __truediv__(self, otro: "Fraccion") -> "Fraccion":
        resultado_numerador = self.__numerador * otro.__denominador
        resultado_denominador = self.__denominador * otro.__numerador
        return Fraccion(resultado_numerador, resultado_denominador) # type: ignore

    def __floordiv__(self, otro: "Fraccion") -> "Fraccion":
        raise ArithmeticError()

    def __ge__(self, otro: "Fraccion") -> bool:
        """ Igualo denominador para poder comparar """
        num1 = self.__numerador * otro.__denominador
        num2 = otro.__numerador * self.__denominador

        return num1 >= num2 # type: ignore

    def __lt__(self, otro: Numero) -> bool:
        return otro.lt_fraccion(self) # type: ignore

    def suma_fraccion(self, otro: Numero):
        """ Suma de otro (fracción) a una fracción """
        if self.__denominador != otro.__denominador: # type: ignore
            raise NotImplementedError("No está implementada la suma con denominadores distintos")

        num = self.__numerador + otro.__numerador # type: ignore
        suma = Fraccion(num, self.__denominador)
        return suma

    def multiplicar_fraccion(self, otro: Numero):
        """ Multiplicación de otro (fracción) a una fracción """
        num = self.__numerador * otro.__numerador     # type: ignore
        den = self.__denominador * otro.__denominador # type: ignore

        if den.__entero != 0 and num.__entero % den.__entero == 0: # type: ignore
            return entero.Entero(num.__entero // den.__entero)        # type: ignore

        return Fraccion(num, den) # type: ignore

    def lt_fraccion(self, otro: Numero):
        """ Retornar si el otro (fracción) es menor que la fracción """
        numerador1 = self.__numerador * otro.__denominador # type: ignore
        numerador2 = otro.__numerador * self.__denominador # type: ignore

        return numerador1 < numerador2 # type: ignore

    def suma_entero(self, otro: Numero):
        """ Suma de otro (entero) a una fracción """
        otro = Fraccion(otro, entero.Entero(1)) # type: ignore
        return otro + self

    def multiplicar_entero(self, otro: Numero):
        """ Multiplicación de otro (entero) a una fracción """
        num = self.__numerador * otro
        den = self.__denominador
        if den.__entero != 0 and num.__entero % den.__entero == 0: #type: ignore
            return entero.Entero(num.__entero // den.__entero) #type: ignore

        return Fraccion(num, den) #type: ignore

    def lt_entero(self, otro: Numero):
        """ Retornar si el otro (entero) es menor que la fracción """
        num = otro * self.__denominador
        return num < self.__numerador

    @property
    def numerador(self):
        """ Property numerador """
        return self.__numerador
    @property
    def denominador(self):
        """  Property denominador """
        return self.__denominador
