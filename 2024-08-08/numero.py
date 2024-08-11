import abc


class Numero(abc.ABC):
    @abc.abstractmethod
    def __str__(self):
        """Retorna la representación del número como texto.
        Ejemplo de uso: str(a)

        Returns:
            string: La representación del número como texto.
        """

    @abc.abstractmethod
    def __repr__(self):
        """Retorna la representación detallada del número como texto.
        Ejemplo de uso: repr(a)

        Returns:
            string: La representación detallada del número como texto.
        """

    @abc.abstractmethod
    def __eq__(self, otro: "Numero") -> bool:
        """Indica si un número es igual a otro.
        Ejemplo de uso: a == b

        Args:
            otro (Numero): el número a comparar.

        Returns:
            bool: true si el número representado es el mismo.
        """

    @abc.abstractmethod
    def __add__(self, otro: "Numero") -> "Numero":
        """Suma dos números.
        Ejemplo de uso: a + b

        Args:
            otro (Numero): el número a sumar.

        Returns:
            Numero: un nuevo número con el resultado de la suma.
        """

    @abc.abstractmethod
    def __sub__(self, otro: "Numero") -> "Numero":
        """Resta dos números.
        Ejemplo de uso: a - b

        Args:
            otro (Numero): el número a restar.

        Returns:
            Numero: un nuevo número con el resultado de la resta.
        """

    @abc.abstractmethod
    def __mul__(self, otro: "Numero") -> "Numero":
        """Multiplica dos números.
        Ejemplo de uso: a * b

        Args:
            otro (Numero): el número a multiplicar.

        Returns:
            Numero: un nuevo número con el resultado de la multiplicación.
        """

    @abc.abstractmethod
    def __truediv__(self, otro: "Numero") -> "Numero":
        """Divide dos números.
        Ejemplo de uso: a / b

        Args:
            otro (Numero): el divisor.

        Returns:
            Numero: un nuevo número con el resultado de la división.
        """

    @abc.abstractmethod
    def __floordiv__(self, otro: "Numero") -> "Numero":
        """Divide dos números con división entera.
        Ejemplo de uso: a // b

        Args:
            otro (Numero): el divisor.

        Returns:
            Numero: un nuevo número con el resultado de la división.
        """

    @abc.abstractmethod
    def __ge__(self, otro: "Numero") -> bool:
        """Indica si un número es mayor o igual a otro.
        Ejemplo de uso: a >= b

        Args:
            otro (Numero): el número a comparar

        Returns:
            bool: True si el número es mayor o igual al otro.
        """

    @abc.abstractmethod
    def __lt__(self, otro: "Numero") -> bool:
        """Indica si un número es menor a otro.
        Ejemplo de uso: a < b

        Args:
            otro (Numero): el número a comparar

        Returns:
            bool: True si el número es menor al otro.
        """
