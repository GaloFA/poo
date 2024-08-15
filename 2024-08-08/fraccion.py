"""Import classes"""

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
        return f"{self.numerador}/{self.denominador}"

    def __repr__(self) -> str:
        return f"Fraccion({self.numerador}/{self.denominador})"

    def __eq__(self, otro: "Fraccion") -> bool:
        return self.numerador == otro.numerador and self.denominador == otro.denominador

    def __add__(self, otro: Numero):
        return otro.suma_fraccion(self) # type: ignore

    def __sub__(self, otro: "Fraccion") -> "Fraccion":
        if self.denominador == otro.denominador:
            temp_numerador = self.numerador - otro.numerador
            return Fraccion(temp_numerador, self.denominador)
        raise NotImplementedError("No está implementada la resta con denominadores distintos")

    def __mul__(self, otro: Numero):
        return otro.multiplicar_fraccion(self) # type: ignore

    def __truediv__(self, otro: "Fraccion") -> "Fraccion":
        resultado_numerador = self.numerador * otro.denominador
        resultado_denominador = self.denominador * otro.numerador
        return Fraccion(resultado_numerador, resultado_denominador) # type: ignore

    def __floordiv__(self, otro: "Fraccion") -> "Fraccion":
        raise ArithmeticError()

    def __ge__(self, otro: "Fraccion") -> bool:
        """ Igualo denominador para poder comparar """
        num1 = self.numerador * otro.denominador
        num2 = otro.numerador * self.denominador

        return num1 >= num2 # type: ignore

    def __lt__(self, otro: Numero) -> bool:
        return otro.lt_fraccion(self) # type: ignore

    def suma_fraccion(self, otro: Numero):
        """ Suma de otro (entero o fracción) a una fracción """
        if self.denominador == otro.denominador: # type: ignore
            num = self.numerador + otro.numerador # type: ignore
            suma = Fraccion(num, self.denominador)
            return suma
        raise NotImplementedError("No está implementada la suma con denominadores distintos")

    def multiplicar_fraccion(self, otro: Numero):
        """ Multiplicación de otro (entero o fracción) a una fracción """
        num = self.numerador * otro.numerador     # type: ignore
        den = self.denominador * otro.denominador # type: ignore

        if den.entero != 0 and num.entero % den.entero == 0: # type: ignore
            return entero.Entero(num.entero // den.entero)        # type: ignore

        return Fraccion(num, den) # type: ignore

    def lt_fraccion(self, otro: Numero):
        """ Retornar si el otro es menor que la fracción """
        numerador1 = self.numerador * otro.denominador # type: ignore
        numerador2 = otro.numerador * self.denominador # type: ignore

        return numerador1 < numerador2 # type: ignore

    def suma_entero(self, otro: Numero):
        otro = Fraccion(otro, entero.Entero(1))
        return otro + self

    def multiplicar_entero(self, otro: Numero):
        num = self.numerador * otro
        den = self.denominador
        if den.entero != 0 and num.entero % den.entero == 0: #type: ignore
            return entero.Entero(num.entero // den.entero) #type: ignore
        return Fraccion(num, den) #type: ignore

    def lt_entero(self, otro: Numero):
        num = otro * self.denominador
        return num < self.numerador

    @property
    def numerador(self):
        """ Property numerador """
        return self.__numerador
    @property
    def denominador(self):
        """  Property denominador """
        return self.__denominador
