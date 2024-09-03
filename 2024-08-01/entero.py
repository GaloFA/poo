#type: ignore pylint: skip-file
class Entero:
    def __init__(self, value: int):
        self.__value = value

    def valor_string(self) -> str:
        return str(self.__value)

    def suma(self, other_value: "Entero"):
        answer = self.__value + other_value.__value
        return Entero(answer)
    
    def resta(self, other_value: "Entero"):
        answer = self.__value - other_value.__value
        return Entero(answer)
    
    def multiplicacion(self, other_value: "Entero"):
        answer = self.__value * other_value.__value
        return Entero(answer)
    
    def division(self, other_value: "Entero"):
        answer = self.__value // other_value.__value
        return Entero(answer)
    
    def mayor(self, other_value: "Entero"):
        answer = self.__value > other_value.__value
        return answer
    
    def mayor_igual(self, other_value: "Entero"):
        answer = self.__value >= other_value.__value
        return answer
    
    def menor(self, other_value: "Entero"):
        answer = self.__value < other_value.__value
        return answer
    
    def menor_igual(self, other_value: "Entero"):
        answer = self.__value <= other_value.__value
        return answer
    
    def negativo(self):
        answer = self.__value < 0
        return answer
    
    def positivo(self):
        answer = self.__value > 0
        return answer
    
    def igual_a_cero(self):
        answer = self.__value == 0
        return answer