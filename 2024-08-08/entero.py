from numero import Numero

class Entero(Numero):
    def __init__(self, entero: int):
        self.__entero: int = entero

    def __str__(self) -> str:
        return str(self.__entero)

    def __repr__(self) -> str:
        return f"Entero({self.__entero})"

    def __eq__(self, otro: "Entero") -> bool:
        return self.__entero == otro.__entero

    def __add__(self, otro):
        from fraccion import Fraccion
        if isinstance(otro, Fraccion):
            num = Entero(int(self.__entero) * int(str(otro.denominador)) + int(str(otro.numerador)))
            return Fraccion(num, otro.denominador)
        elif isinstance(otro, Entero):
            return Entero(self.__entero + otro.__entero)

    def __sub__(self, otro: "Entero") -> "Entero":
        return Entero(self.__entero - otro.__entero)

    def __mul__(self, otro):
        from fraccion import Fraccion
        if isinstance(otro, Fraccion):
            if int(str(self.__entero)) % int(str(otro.denominador)) == 0:
                ans = (int(str(self.__entero)) * int(str(otro.numerador))) // int(str(otro.denominador)) 
                return Entero(ans)
            else:
                num = Entero(int(str(self.__entero)) * int(str(otro.numerador)))
                return Fraccion(num, otro.__denominador)
        elif isinstance(otro, Entero):
            return Entero(self.__entero * otro.__entero)
        
    def __truediv__(self, otro: "Entero"):
        from fraccion import Fraccion
        if otro.__entero == 0:
            raise ZeroDivisionError("No se puede dividir por cero")        
        elif self.__entero % otro.__entero != 0:
            return Fraccion(Entero(self.__entero), Entero(otro.__entero))
        else: 
            return Entero(self.__entero // otro.__entero)

    def __floordiv__(self, otro: "Entero") -> "Entero":
        return Entero(self.__entero // otro.__entero)

    def __ge__(self, otro: "Entero") -> bool:
        return self.__entero >= otro.__entero

    def __lt__(self, otro: "Entero") -> bool:
        return self.__entero < otro.__entero
    
    @property
    def entero (self):
        return self.__entero