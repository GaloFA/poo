""" a """

import unittest
from entero import Entero
from fraccion import Fraccion



class TestFraccion(unittest.TestCase):
    """ a """

    def test_inicializar_sin_tipo_entero_da_error(self):
        """ a """
        with self.assertRaises(ValueError):
            Fraccion(1, 2)  # type: ignore

    def test_inicializar_con_denominador_cero_da_error(self):
        """ a """
        with self.assertRaises(ZeroDivisionError):
            Fraccion(Entero(1), Entero(0))

    def test_str(self):
        """ a """
        f1 = Fraccion(Entero(5), Entero(2))

        self.assertEqual("5/2", str(f1))

    def test_repr(self):
        """ a """
        f1 = Fraccion(Entero(5), Entero(2))

        self.assertEqual("Fraccion(5/2)", repr(f1))

    def test_suma(self):
        """ a """
        f1 = Fraccion(Entero(2), Entero(2))
        f2 = Fraccion(Entero(1), Entero(2))
        res = Fraccion(Entero(3), Entero(2))

        self.assertEqual(res, f1 + f2)

    def test_resta(self):
        """ a """
        f1 = Fraccion(Entero(2), Entero(2))
        f2 = Fraccion(Entero(1), Entero(2))

        res = Fraccion(Entero(1), Entero(2))
        self.assertEqual(res, f1 - f2)

    def test_multiplicacion(self):
        """ a """
        f1 = Fraccion(Entero(2), Entero(2))
        f2 = Fraccion(Entero(1), Entero(2))

        res = Fraccion(Entero(2), Entero(4))
        self.assertEqual(res, f1 * f2)

    def test_division(self):
        """ a """
        f1 = Fraccion(Entero(2), Entero(2))
        f2 = Fraccion(Entero(1), Entero(2))

        res = Fraccion(Entero(4), Entero(2))
        self.assertEqual(res, f1 / f2)

    def test_mayor_o_igual_retorna_verdadero_si_es_mayor(self):
        """ a """
        f1 = Fraccion(Entero(4), Entero(2))
        f2 = Fraccion(Entero(1), Entero(3))

        self.assertTrue(f1 >= f2)

    def test_mayor_o_igual_retorna_verdadero_si_es_igual(self):
        """ a """
        f1 = Fraccion(Entero(4), Entero(2))
        f2 = Fraccion(Entero(4), Entero(2))

        self.assertTrue(f1 >= f2)

    def test_mayor_o_igual_retorna_falso_si_es_menor(self):
        """ a """
        f1 = Fraccion(Entero(1), Entero(2))
        f2 = Fraccion(Entero(4), Entero(3))

        self.assertFalse(f1 >= f2)

    def test_menor_retorna_verdadero_si_es_menor(self):
        """ a """
        f1 = Fraccion(Entero(1), Entero(2))
        f2 = Fraccion(Entero(4), Entero(3))

        self.assertTrue(f1 < f2)

    def test_menor_retorna_falso_si_es_mayor(self):
        """ a """
        f1 = Fraccion(Entero(4), Entero(2))
        f2 = Fraccion(Entero(1), Entero(3))

        self.assertFalse(f1 < f2)

    def test_menor_retorna_falso_si_es_igual(self):
        """ a """
        f1 = Fraccion(Entero(4), Entero(2))
        f2 = Fraccion(Entero(4), Entero(2))

        self.assertFalse(f1 < f2)

    def test_division_entero_error(self):
        """ a """
        with self.assertRaises(ArithmeticError):
            f1 = Fraccion(Entero(1), Entero(2))
            f2 = Fraccion(Entero(1), Entero(4))

            f1 // f2 # type: ignore pylint: disable=pointless-statement

if __name__ == "__main__":
    unittest.main()
