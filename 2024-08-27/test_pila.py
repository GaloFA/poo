# pylint: skip-file
import unittest
from pila import Pila, PilaLlena, PilaVacia, PilaConPrioridad, ValorPrioridadInvalido


class TestPila(unittest.TestCase):

    def test_01_pila_llena(self):
        pila = Pila(2)

        pila.apilar('A')
        pila.apilar('B')

        with self.assertRaises(PilaLlena):
            pila.apilar('C')

    def test_02_pila_vacia(self):
        pila = Pila(2)

        with self.assertRaises(PilaVacia):
            pila.desapilar()

    def test_03_len_pila(self):
        pila = Pila(3)

        pila.apilar('A')
        pila.apilar('B')
        pila.apilar('C')
        length = len(pila)

        self.assertEqual(3, length)

    def test_04_iterador_devuelve_resultado_en_orden_de_salida(self):
        pila = Pila(3)

        pila.apilar('A')
        pila.apilar('B')
        pila.apilar('C')
        elementos = list(pila)

        self.assertEqual(elementos, ['C', 'B', 'A'])

    def test_05_reversed(self):
        pila = Pila(3)

        pila.apilar('A')
        pila.apilar('B')
        pila.apilar('C')
        elementos = list(reversed(pila))

        self.assertEqual(elementos, ['A', 'B', 'C'])

class TestPilaConPrioridad(unittest.TestCase):
    
    def test_01_apilar_elemento_si_es_prioridad_valida(self):
        pila = PilaConPrioridad(3, 2)

        pila.apilar_prioridad(1, 1)
        pila.apilar_prioridad(2, 0)

        self.assertEqual(len(pila), 2)

    def test_02_apilar_elemento_prioridad_invalida_da_error(self):
        pila = PilaConPrioridad(2, 1)

        with self.assertRaises(ValorPrioridadInvalido):
            pila.apilar_prioridad(1, 2)

    def test_03_desapilar_elemento_con_prioridad(self):
        pila = PilaConPrioridad(4, 2)

        pila.apilar_prioridad(1, 0)
        pila.apilar_prioridad(2, 1)
        pila.apilar_prioridad(3, 2)
        pila.apilar_prioridad(4, 2)

        self.assertEqual(pila.desapilar_prioridad(), 4)

    def test_04_len_pila(self):
        pila = PilaConPrioridad(3, 2)

        self.assertEqual(len(pila), 0)

    def test_05_iter_pila(self):
        pila = PilaConPrioridad(4, 2)

        pila.apilar_prioridad(1, 0)
        pila.apilar_prioridad(2, 1)
        pila.apilar_prioridad(3, 2)
        pila.apilar_prioridad(4, 2)
        elementos = [elemento for elemento in pila]

        self.assertEqual(elementos, [4, 3, 2, 1])

    def test_06_iter_pila(self):
        pila = PilaConPrioridad(5, 2)

        pila.apilar_prioridad(1, 0)
        pila.apilar_prioridad(2, 1)
        pila.apilar_prioridad(3, 2)
        pila.apilar_prioridad(5, 1)
        pila.apilar_prioridad(4, 2)
        elementos = [elemento for elemento in pila]

        self.assertEqual(elementos, [4, 3, 5, 2, 1])

if __name__ == "__main__":
    unittest.main()
