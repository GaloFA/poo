""" Clases """
import abc

# Clase abstracta

class PilaAbstracta(abc.ABC): # pylint: disable=missing-class-docstring
    @abc.abstractmethod
    def __len__(self):
        """Retorna la longitud de la colección como número.
        Ejemplo de uso: len(lista)

        Returns:
            integer: La longitud de la colección como número.
        """

    @abc.abstractmethod
    def __iter__(self):
        """Retorna el iterable de la colección como lista.
        Ejemplo de uso: iter(lista)

        Returns:
            list: El iterable de la colección como lista.
        """

    @abc.abstractmethod
    def __reversed__(self):
        """Retorna el iterable revertido (en orden de salida) de la colección como lista.
        Ejemplo de uso: reversed(lista)

        Returns:
            list: El iterable revertido (en orden de salida) de la colección como lista.
        """

# Clases

class Pila(PilaAbstracta):
    """ Clase pila """
    def __init__(self, capacidad_maxima):
        self.__capacidad_maxima = capacidad_maxima
        self.__elementos = []

    def apilar(self, elemento):
        """ Método para apilar elementos """
        if len(self.__elementos) >= self.__capacidad_maxima:
            raise PilaLlena("La pila está llena.")
        self.__elementos.append(elemento)

    def desapilar(self):
        """ Método para desapilar elementos """
        if not self.__elementos:
            raise PilaVacia("La pila está vacía.")

        return self.__elementos.pop()

    def __len__(self):
        return len(self.__elementos)

    def __iter__(self):
        return reversed(self.__elementos)

    def __reversed__(self):
        return iter(self.__elementos)

class PilaConPrioridad(PilaAbstracta):
    """ Clase de Pila con Prioridad """
    def __init__(self, capacidad_maxima, max_prioridad):
        self.__pila = Pila(capacidad_maxima)
        self.__max_prioridad = max_prioridad

    def apilar_prioridad(self, elemento, prioridad):
        """ Método para apilar elementos con prioridad """
        if prioridad < 0 or prioridad > self.__max_prioridad:
            raise ValorPrioridadInvalido("Prioridad no válida")

        if len(self.__pila) >= self.__pila._Pila__capacidad_maxima: # type: ignore pylint: disable=protected-access
            raise PilaLlena("La pila está llena")

        self.__pila.apilar((elemento, prioridad))

    def desapilar_prioridad(self):
        """ Método para desapilar elementos con prioridad """
        if len(self.__pila) == 0:
            raise PilaVacia("La pila está vacía")

        max_prioridad = -1
        index_max_prioridad = -1
        length = len(self.__pila)

        elementos = list(reversed(self.__pila))
        for i in range(length):
            prioridad = elementos[i][1]
            if prioridad >= max_prioridad:
                max_prioridad = prioridad
                index_max_prioridad = i

        return elementos.pop(index_max_prioridad)[0]

    def __len__(self):
        return len(self.__pila)

    def __iter__(self):
        elementos_ordenados = []
        elementos = list(self.__pila)

        for prioridad_actual in range(self.__max_prioridad, -1, -1):
            for elemento, prioridad in elementos:
                if prioridad == prioridad_actual:
                    elementos_ordenados.append(elemento)

        return iter(elementos_ordenados)

    def __reversed__(self):
        return reversed(self.__pila)

# Excepciones

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
