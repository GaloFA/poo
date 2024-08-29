""" Clases """

class PilaLlena(Exception):
    """ Error de pila llena """
    def __init__(self, message):
        pass

class PilaVacia(Exception):
    """ Error de pila vacía """
    def __init__(self, message):
        pass

class ValorPrioridadInvalido(Exception):
    """ Error de nivel de prioridad inválida """
    def __init__(self, message):
        pass

class Pila:
    """ Clase pila """
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.elementos = []

    def apilar(self, elemento):
        """ Método para apilar elementos """
        if len(self.elementos) >= self.capacidad_maxima:
            raise PilaLlena("La pila está llena.")
        self.elementos.append(elemento)

    def desapilar(self):
        """ Método para desapilar elementos """
        if not self.elementos:
            raise PilaVacia("La pila está vacía.")

        return self.elementos.pop()

    def __len__(self):
        return len(self.elementos)

    def __iter__(self):
        return reversed(self.elementos)

    def __reversed__(self):
        return iter(self.elementos)

class PilaConPrioridad:
    """ Clase de Pila con Prioridad """
    def __init__(self, capacidad_maxima, max_prioridad):
        self.capacidad_maxima = capacidad_maxima
        self.max_prioridad = max_prioridad
        self.elementos = []

    def apilar_prioridad(self, elemento, prioridad):
        """ Método para apilar elementos """
        if prioridad < 0 or prioridad > self.max_prioridad:
            raise ValorPrioridadInvalido("Prioridad no válida")

        if len(self.elementos) >= self.capacidad_maxima:
            raise PilaLlena("La pila está llena")

        self.elementos.append((elemento, prioridad))

    def desapilar_prioridad(self):
        """ Método para desapilar elementos """
        if not self.elementos:
            raise PilaVacia("La pila está vacía")

        max_prioridad = -1
        index_max_prioridad = -1
        length = len(self.elementos)

        for i in range(length):
            prioridad = self.elementos[i][0]
            if prioridad >= max_prioridad:
                max_prioridad = prioridad
                index_max_prioridad = i

        return self.elementos.pop(index_max_prioridad)[0]

    def __len__(self):
        return len(self.elementos)

    def __iter__(self):
        elementos_ordenados = []

        for prioridad_actual in range(self.max_prioridad, -1, -1):
            for elemento, prioridad in self.elementos:
                if prioridad == prioridad_actual:
                    elementos_ordenados.append(elemento)

        return iter(elementos_ordenados)
