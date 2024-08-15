"""Error"""


class SinPiernasError(Exception):
    """Error si no activo las piernas"""

    def __init__(self, message):
        self.message = message


class Pepita:  # pylint: disable=missing-class-docstring
    def __init__(self, piernas):
        self._piernas = piernas

    def saludar(self):
        """Saluda a la gente"""
        print("Hola!!!")

    def saludar_de_nuevo(self):
        """Saluda de nuevo"""
        print("hola de nuevo")

    def activar_piernas(self):
        """Activa las piernas"""
        self._piernas = True

    def desactivar_piernas(self):
        """Desactiva las piernas"""
        self._piernas = False

    def piernas_activadas(self):
        """Dice si las piernas estan activadas"""
        return self._piernas

    def correr(self):
        """Dice si está corriendo o no activo las piernas"""
        if self.piernas_activadas():
            return "Estoy corriendo"
        raise SinPiernasError("")
