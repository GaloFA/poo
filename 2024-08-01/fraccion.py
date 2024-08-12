from entero import Entero
from math import gcd

class FraccionInvalidaError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Fraccion:
    def __init__(self, num_value: Entero, den_value: Entero):
        self.__num_value = num_value
        self.__den_value = den_value
        self.fraccion_valida()

    def fraccion_valida(self):
        if self.__den_value.igual_a_cero():
            raise FraccionInvalidaError("Denominador = 0")

    def valor_fraccion(self):
        return f"{self.__num_value.valor_string()}/{self.__den_value.valor_string()}"

    def calcular_divisor_comun_maximo(self, valor1: Entero, valor2: Entero):
        # Convertir a INT
        v1 = int(valor1.valor_string())
        v2 = int(valor2.valor_string())
        
        #Devolver el DCM
        return gcd(v1, v2)
        
    def simplificar_fraccion(self):
       # Calcular el DCM
        dcm = self.calcular_divisor_comun_maximo(self.__num_value, self.__den_value)
        
        # Convertir a INT
        num = int(self.__num_value.valor_string())
        den = int(self.__den_value.valor_string())
        
        # Simplificar la fracción
        num = num // dcm
        den = den // dcm
        
        # Convertir de nuevo a Entero
        num = Entero(num)
        den = Entero(den)
        
        return Fraccion(num, den).valor_fraccion()
    
    def equivalencia_de_fracciones(self, fraccion1: "Fraccion", fraccion2: "Fraccion"):
        # Simplificar las fracciones
        f1_simplificada = fraccion1.simplificar_fraccion()
        f2_simplificada = fraccion2.simplificar_fraccion()
        
        # Comparar las fracciones simplificadas
        return f1_simplificada == f2_simplificada
            
    def sumar_fracciones(self, fraccion: "Fraccion") -> "Fraccion":
        # Establecer los numeradores y denominadores
        num1 = int(self.__num_value.valor_string())
        den1 = int(self.__den_value.valor_string())
        num2 = int(fraccion.__num_value.valor_string())
        den2 = int(fraccion.__den_value.valor_string())
        
        # Calcular los nuevos numeradores y denominadores
        num = num1 * den2 + num2 * den1
        den = den1 * den2
        
        # Retornar el resultado en forma de fracción simplificada
        return Fraccion(Entero(num), Entero(den)).simplificar_fraccion()
        
    def restar_fracciones(self, fraccion: "Fraccion") -> "Fraccion":
        # Establecer los numeradores y denominadores
        num1 = int(self.__num_value.valor_string())
        den1 = int(self.__den_value.valor_string())
        num2 = int(fraccion.__num_value.valor_string())
        den2 = int(fraccion.__den_value.valor_string())
        
        # Calcular los nuevos numeradores y denominadores
        num = num1 * den2 - num2 * den1
        den = den1 * den2
        
        # Retornar el resultado en forma de fracción simplificada
        return Fraccion(Entero(num), Entero(den)).simplificar_fraccion()

    def multiplicar_fracciones(self, fraccion: "Fraccion") -> "Fraccion":
        # Establecer los numeradores y denominadores
        num1 = int(self.__num_value.valor_string())
        den1 = int(self.__den_value.valor_string())
        num2 = int(fraccion.__num_value.valor_string())
        den2 = int(fraccion.__den_value.valor_string())
        
        # Calcular los nuevos numeradores y denominadores
        num = num1 * num2
        den = den1 * den2
        
        # Retornar el resultado en forma de fracción simplificada
        return Fraccion(Entero(num), Entero(den)).simplificar_fraccion()

    def dividir_fracciones(self, fraccion: "Fraccion") -> "Fraccion":
        # Establecer los numeradores y denominadores
        num1 = int(self.__num_value.valor_string())
        den1 = int(self.__den_value.valor_string())
        num2 = int(fraccion.__num_value.valor_string())
        den2 = int(fraccion.__den_value.valor_string())
        
        # Calcular los nuevos numeradores y denominadores
        num = num1 * den2
        den = den1 * num2
        
        # Retornar el resultado en forma de fracción simplificada
        return Fraccion(Entero(num), Entero(den)).simplificar_fraccion()        