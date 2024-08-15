"""Import classes"""

from numero import Numero
import entero as e

class Fraccion(Numero):
    """ Clase Fraccion """
    def __init__(self, numerador: e.Entero, denominador: e.Entero):
        if not isinstance(numerador, e.Entero):
            raise ValueError("El numerador debe ser de tipo Entero")

        if not isinstance(denominador, e.Entero):
            raise ValueError("El denominador debe ser de tipo Entero")

        if denominador == e.Entero(0):
            raise ZeroDivisionError("El denominador no puede ser cero")

        self.__numerador: e.Entero = numerador
        self.__denominador: e.Entero = denominador

    def __str__(self) -> str:
        return f"{self.numerador}/{self.denominador}"

    def __repr__(self) -> str:
        return f"Fraccion({self.numerador}/{self.denominador})"

    def __eq__(self, otro: "Fraccion") -> bool:
        return self.numerador == otro.numerador and self.denominador == otro.denominador

    def __add__(self, otro):
        if isinstance(otro, e.Entero):
            num = e.Entero(int(otro.entero) * int(str(self.denominador)) + int(str(self.numerador)))
            return Fraccion(num, self.denominador)
        if isinstance(otro, Fraccion):
            if self.denominador == otro.denominador:
                temp_numerador = e.Entero(int(str(self.numerador + otro.numerador)))
                return Fraccion(temp_numerador, self.denominador)
            raise NotImplementedError("No está implementada la suma con denominadores distintos")

    def __sub__(self, otro: "Fraccion") -> "Fraccion":
        if self.denominador == otro.denominador:
            temp_numerador = self.numerador - otro.numerador
            return Fraccion(temp_numerador, self.denominador)
        raise NotImplementedError("No está implementada la resta con denominadores distintos")

    def __mul__(self, otro):
        if isinstance(otro, Fraccion):
            resultado_numerador = e.Entero(int(str(self.numerador * otro.numerador)))
            resultado_denominador = e.Entero(int(str(self.denominador * otro.denominador)))
            return Fraccion(resultado_numerador, resultado_denominador)

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

        return num1 >= num2 #type: ignore

    def __lt__(self, otro) -> bool: # type: ignore
        """ Igualo denominador para poder comparar """
        if isinstance(otro, Fraccion):
            num1 = self.numerador * otro.denominador
            num2 = otro.numerador * self.denominador

            return num1 < num2 #type: ignore
        elif isinstance(otro, e.Entero):
            num1 = otro.entero * self.denominador # type: ignore
            return num1 < self.numerador #type: ignore}

    def suma_fraccion(self, otro: Numero):
        """ Suma de otro (entero o fracción) a una fracción """
        if self.denominador == otro.denominador: #type: ignore
            num = self.numerador + otro.numerador #type: ignore
            suma = Fraccion(num, self.denominador)
            return suma
        raise NotImplementedError("No está implementada la suma con denominadores distintos")

    def _multiplicar_fraccion(self, otro: Numero):
        """ Multiplicación de otro (entero o fracción) a una fracción """
        num = self.numerador * otro.numerador     #type: ignore
        den = self.denominador * otro.denominador #type: ignore

        if den.entero != 0 and num.entero % den.entero == 0: #type: ignore
            return e.Entero(num.entero // den.entero)        #type: ignore

        return Fraccion(num, den) #type: ignore

    @property
    def numerador(self):
        """ Property numerador """
        return self.__numerador
    @property
    def denominador(self):
        """  Property denominador """
        return self.__denominador
