# pylint: skip-file
import unittest
from pila import Pila, PilaLlena, PilaVacia, PilaConPrioridad, ValorPrioridadInvalido


class TestPila(unittest.TestCase):

    def test_pila_llena(self):
        pila = Pila(2)
        pila.apilar('A')
        pila.apilar('B')
        with self.assertRaises(PilaLlena):
            pila.apilar('C')

    def test_pila_vacia(self):
        pila = Pila(2)
        with self.assertRaises(PilaVacia):
            pila.desapilar()

    def test_len_pila(self):
        pila = Pila(3)
        pila.apilar('A')
        pila.apilar('B')
        pila.apilar('C')

        length = len(pila)

        self.assertEqual(3, length)

    def test_iterador(self):
        pila = Pila(3)
        pila.apilar('A')
        pila.apilar('B')
        pila.apilar('C')
        elementos = list(iter(pila))

        self.assertEqual(elementos, ['C', 'B', 'A'])

    def test_reversed(self):
        pila = Pila(3)
        pila.apilar('A')
        pila.apilar('B')
        pila.apilar('C')
        elementos = list(reversed(pila))
        self.assertEqual(elementos, ['A', 'B', 'C'])

class TestPilaConPrioridad(unittest.TestCase):
    
    def test_apilar_elemento_prioridad_valida(self):
        pila = PilaConPrioridad(3, 2)  # Máxima prioridad soportada: 2
        pila.apilar(1, 1)
        pila.apilar(2, 0)
        self.assertEqual(len(pila), 2)

    def test_apilar_elemento_prioridad_invalida(self):
        pila = PilaConPrioridad(2, 1)  # Máxima prioridad soportada: 1
        with self.assertRaises(ValorPrioridadInvalido):
            pila.apilar(1, 2)

    def test_desapilar_elemento_prioridad(self):
        pila = PilaConPrioridad(4, 2)
        pila.apilar(1, 0)
        pila.apilar(2, 1)
        pila.apilar(3, 2)
        pila.apilar(4, 2)
        self.assertEqual(pila.desapilar(), 4)  # Prioridad más alta
        self.assertEqual(pila.desapilar(), 3)  # Prioridad más alta

    def test_desapilar_elemento_prioridades_iguales(self):
        pila = PilaConPrioridad(3, 2)
        pila.apilar(1, 1)
        pila.apilar(2, 1)
        self.assertEqual(pila.desapilar(), 2)  # Último de la misma prioridad

    def test_len_pila(self):
        pila = PilaConPrioridad(3, 2)
        self.assertEqual(len(pila), 0)
        pila.apilar(1, 1)
        self.assertEqual(len(pila), 1)
        pila.desapilar()
        self.assertEqual(len(pila), 0)

    def test_iter_pila(self):
        pila = PilaConPrioridad(4, 2)
        pila.apilar(1, 0)
        pila.apilar(2, 1)
        pila.apilar(3, 2)
        pila.apilar(4, 2)
        elementos = [elemento for elemento in pila]
        self.assertEqual(elementos, [3, 4, 2, 1])  # Elementos en orden de desapilado

if __name__ == "__main__":
    unittest.main()
