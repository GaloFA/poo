"""Import classes"""
# pylint: disable=protected-access, line-too-long

from numero import Numero
import entero

class Fraccion(Numero):
    """ Clase Fraccion """
    def __init__(self, numerador: "entero.Entero", denominador: "entero.Entero"):
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
        return self.__numerador == otro._Fraccion__numerador and self.__denominador == otro._Fraccion__denominador # type: ignore

    def __add__(self, otro: Numero):
        return otro.suma_fraccion(self) # type: ignore

    def __sub__(self, otro: "Fraccion") -> "Fraccion":

        if self.__denominador != otro._Fraccion__denominador: # type: ignore
            temp_numerador = entero.Entero(self.__numerador * otro.__denominador + otro.__numerador * self.__denominador) # type: ignore
            temp_denominador = entero.Entero(self.__denominador * otro.__denominador) # type: ignore
            return Fraccion(temp_numerador, temp_denominador)

        temp_numerador = self.__numerador - otro._Fraccion__numerador # type: ignore
        return Fraccion(temp_numerador, self.__denominador)

    def __mul__(self, otro: Numero):
        return otro.multiplicar_fraccion(self) # type: ignore

    def __truediv__(self, otro: "Fraccion") -> "Fraccion":
        resultado_numerador = self.__numerador * otro._Fraccion__denominador # type: ignore
        resultado_denominador = self.__denominador * otro._Fraccion__numerador # type: ignore
        return Fraccion(resultado_numerador, resultado_denominador) # type: ignore

    def __floordiv__(self, otro: "Fraccion") -> "Fraccion":
        raise ArithmeticError()

    def __ge__(self, otro: "Fraccion") -> bool:
        """ Igualo denominador para poder comparar """
        num1 = self.__numerador * otro._Fraccion__denominador # type: ignore
        num2 = otro._Fraccion__numerador * self.__denominador # type: ignore

        return num1 >= num2 # type: ignore

    def __lt__(self, otro: Numero) -> bool:
        return otro.lt_fraccion(self) # type: ignore

    def suma_fraccion(self, otro):
        """ Suma de otro (fracción) a una fracción """

        return Fraccion(self.__numerador  + otro._Fraccion__numerador, self.__denominador) # type: ignore

    def suma_entero(self, otro):
        """ Suma de otro (entero) a una fracción """

        otro_fraccion = Fraccion(otro, entero.Entero(1))
        numerador_final = self.__numerador * otro_fraccion._Fraccion__denominador + self.__denominador * otro_fraccion._Fraccion__numerador # type: ignore
        denominador_final = self.__denominador * otro_fraccion._Fraccion__denominador # type: ignore
        return Fraccion(numerador_final, denominador_final)

    def multiplicar_fraccion(self, otro: Numero):
        """ Multiplicación de otro (fracción) a una fracción """

        numerador_final = self.__numerador * otro._Fraccion__numerador # type: ignore
        denominador_final = self.__denominador * otro._Fraccion__denominador # type: ignore
        return Fraccion(numerador_final, denominador_final)

    def multiplicar_entero(self, otro):
        """ Multiplicación de otro (entero) a una fracción """

        if otro.entero % self.__denominador.__entero == 0:
            return self.__numerador
        else:
            otro_fraccion = Fraccion(otro, entero.Entero(1))
            numerador_final = self.__numerador * otro_fraccion.__numerador
            denominador_final = self.__denominador * otro_fraccion.__denominador
        return Fraccion(numerador_final, denominador_final) # type: ignore

    def lt_entero(self, otro):
        """ Retornar si el otro (entero) es menor que la fracción """
        otro_fraccion = Fraccion(otro, entero.Entero(1)) #type: ignore

        self_fraccion = Fraccion(self.__numerador * otro_fraccion.__denominador, self.__denominador * otro_fraccion.__denominador) # type: ignore
        otro_fraccion = Fraccion(otro_fraccion.__numerador * otro_fraccion.__denominador, otro_fraccion.__denominador * self_fraccion.__denominador) # type: ignore

        return self_fraccion.__numerador > otro_fraccion.__numerador # type: ignore

    def lt_fraccion(self, otro):
        """ Retornar si el otro (fracción) es menor que la fracción """

        self_fraccion = Fraccion(self.__numerador * otro.__denominador, self.__denominador * otro.__denominador)
        otro_fraccion = Fraccion(otro.__numerador * otro.__denominador, otro.__denominador * self.__denominador)

        return self_fraccion.__numerador > otro_fraccion.__numerador
