#type: ignore pylint: skip-file
from entero import Entero

class Rango:
    def __init__(self, limInf: Entero, limSup: Entero):
        self.__limInf = limInf
        self.__limSup = limSup
        
    def representar_en_string(self):
        # Transformar los valores límite en string
        strLimInf = self.__limInf.valor_string()
        strLimSup = self.__limSup.valor_string()
        
        # Retornar en el formato de la consigna (Como si fuera una lista)
        return str(f"[{strLimInf}, {strLimSup}]")
    
    def entero_dentro_de_limites(self, numero: Entero):
        # Convertir a INT todos los valores a utilizar
        num = int(numero.valor_string())
        limInf_int = int(self.__limInf.valor_string())
        limSup_int = int(self.__limSup.valor_string())
        
        # Retornar si el entero recibido se encuentra en el rango
        return limInf_int <= num <= limSup_int
    
    def tamaño_rango(self):
        # Retornar la distancia entre el límite superior y el inferior
        ans = int(self.__limSup.valor_string()) - int(self.__limInf.valor_string())
        ans_str = Entero(ans).valor_string()
        return ans_str
    
    def esta_incluido_en(self, rango2: "Rango"):
        # Convertir los valores a INT
        limInf_int_1 = int(self.__limInf.valor_string())
        limSup_int_1 = int(self.__limSup.valor_string())
        limInf_int_2 = int(rango2.__limInf.valor_string())
        limSup_int_2 = int(rango2.__limSup.valor_string())
        
        # Retornar si un rango esta incluído en otro rango (true o false)
        return limInf_int_2 <= limInf_int_1 and limSup_int_1 <= limSup_int_2
    
    def intersecta_con(self, rango2: "Rango"):
        # Convertir los valores a INT
        limInf_int_1 = int(self.__limInf.valor_string())
        limSup_int_1 = int(self.__limSup.valor_string())
        limInf_int_2 = int(rango2.__limInf.valor_string())
        limSup_int_2 = int(rango2.__limSup.valor_string())
        
        # Retornar si los rangos intersectan (true o falee)
        return not (limSup_int_1 < limInf_int_2 or limInf_int_1 > limSup_int_2)