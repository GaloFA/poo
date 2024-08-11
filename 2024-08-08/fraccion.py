from numero import Numero
import entero as e

class Fraccion(Numero):
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
        return f"{self.__numerador}/{self.__denominador}"
    
    def __repr__(self) -> str:
        return f"Fraccion({self.__numerador}/{self.__denominador})"

    def __eq__(self, otro: "Fraccion") -> bool:
        return self.__numerador == otro.__numerador and self.__denominador == otro.__denominador


    def __add__(self, otro):
        from entero import Entero
        if isinstance(otro, Entero):
            num = Entero(int(otro.__entero) * int(str(self.__denominador)) + int(str(self.__numerador)))
            return Fraccion(num, self.__denominador)
        elif isinstance(otro, Fraccion):
            if self.__denominador == otro.__denominador:
                temp_numerador = Entero(int(str(self.__numerador + otro.__numerador)))
                return Fraccion(temp_numerador, self.__denominador)
            else:
                raise NotImplementedError("No está implementada la suma con denominadores distintos")
        
    def __sub__(self, otro: "Fraccion") -> "Fraccion":
        if self.__denominador == otro.__denominador:
            temp_numerador = self.__numerador - otro.__numerador
            return Fraccion(temp_numerador, self.__denominador)
        else:
            raise NotImplementedError("No está implementada la resta con denominadores distintos")

    def __mul__(self, otro):
        from entero import Entero
        if isinstance(otro, Fraccion):
            resultado_numerador = Entero(int(str(self.__numerador * otro.__numerador)))
            resultado_denominador = Entero(int(str(self.__denominador * otro.__denominador)))
            return Fraccion(resultado_numerador, resultado_denominador)
        elif isinstance(otro, Entero):
            if int(str(otro.__entero)) % int(str(self.__denominador)) == 0:
                ans = (int(str(otro.__entero)) * int(str(self.__numerador))) // int(str(self.__denominador))
                return Entero(ans)
            else:
                num = Entero(int(str(otro.__entero)) * int(str(self.__numerador)))
                return Fraccion(num, self.__denominador)

    def __truediv__(self, otro: "Fraccion") -> "Fraccion":
        resultado_numerador = self.__numerador * otro.__denominador
        resultado_denominador = self.__denominador * otro.__numerador
        return Fraccion(resultado_numerador, resultado_denominador) # type: ignore

    def __floordiv__(self, otro: "Fraccion") -> "Fraccion":
        raise ArithmeticError("No se puede hacer una división entera si el denominador es diferente")
        
    def __ge__(self, otro: "Fraccion") -> bool:
        # Igualo denominador para poder comparar
        num1 = self.__numerador * otro.__denominador
        num2 = otro.__numerador * self.__denominador

        return num1 >= num2 #type: ignore

    def __lt__(self, otro) -> bool: # type: ignore
        from entero import Entero
        # Igualo denominador para poder comparar
        if isinstance(otro, Fraccion):
            num1 = self.__numerador * otro.denominador
            num2 = otro.numerador * self.__denominador

            return num1 < num2 #type: ignore
        elif isinstance(otro, Entero):
            num1 = otro.__entero * self.denominador # type: ignore
            return num1 < self.numerador #type: ignore
        
    @property
    def numerador (self):
        return self.__numerador
    @property
    def denominador(self):
        return self.__denominador