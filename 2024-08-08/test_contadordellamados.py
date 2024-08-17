# pylint: skip-file
import unittest

from contadordellamados import ContadorDeLlamadosDecorator
from entero import Entero
from fraccion import Fraccion


class TestContadorDeLlamados(unittest.TestCase):
    def test_contador_entero_simple(self):
        entero_con_contador = ContadorDeLlamadosDecorator(Entero(10))

        _ = entero_con_contador + Entero(10)

        self.assertEqual(1, entero_con_contador.obtener_contador("__add__"))

    def test_contador_fraccion_simple(self):
        fraccion_con_contador = ContadorDeLlamadosDecorator(
            Fraccion(Entero(10), Entero(2))
        )

        _ = fraccion_con_contador + Fraccion(Entero(10), Entero(2))

        self.assertEqual(1, fraccion_con_contador.obtener_contador("__add__"))

    def test_contador_entero_complejo(self):
        entero_con_contador = ContadorDeLlamadosDecorator(Entero(10))

        for i in range(10):
            entero_con_contador + Entero(i) # type: ignore
            entero_con_contador - Entero(i) # type: ignore

        self.assertEqual(10, entero_con_contador.obtener_contador("__add__"))
        self.assertEqual(10, entero_con_contador.obtener_contador("__sub__"))

    def test_contador_fraccion_complejo(self):
        fraccion_con_contador = ContadorDeLlamadosDecorator(
            Fraccion(Entero(10), Entero(2))
        )

        for i in range(10):
            fraccion_con_contador + Fraccion(Entero(i), Entero(99)) # type: ignore
            fraccion_con_contador - Fraccion(Entero(i), Entero(99)) # type: ignore

        self.assertEqual(10, fraccion_con_contador.obtener_contador("__add__"))
        self.assertEqual(10, fraccion_con_contador.obtener_contador("__sub__"))