# pylint: skip-file
import unittest
from juego import Juego
from tablero import Tablero
from casillero import Casillero
from jugador import Jugador
from verificador import Verificador

class TestJuego(unittest.TestCase):
    
    def test_01_instancia(self):
        juego = Juego()

        self.assertIsInstance(juego, Juego)


if __name__ == "__main__":
    unittest.main()