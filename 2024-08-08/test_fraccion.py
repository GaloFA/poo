""" a """

import unittest
import entero as e
import fraccion as f



class TestFraccion(unittest.TestCase):
    """ a """

    def test_inicializar_sin_tipo_entero_da_error(self):
        """ a """
        with self.assertRaises(ValueError):
            f.Fraccion(1, 2)  # type: ignore

    def test_inicializar_con_denominador_cero_da_error(self):
        """ a """
        with self.assertRaises(ZeroDivisionError):
            f.Fraccion(e.Entero(1), e.Entero(0))

    def test_str(self):
        """ a """
        fraccion = f.Fraccion(e.Entero(5), e.Entero(2))

        self.assertEqual("5/2", str(fraccion))

    def test_repr(self):
        """ a """
        fraccion = f.Fraccion(e.Entero(5), e.Entero(2))

        self.assertEqual("f.Fraccion(5/2)", repr(fraccion))

    def test_suma(self):
        """ a """
        f1 = f.Fraccion(e.Entero(2), e.Entero(2))
        f2 = f.Fraccion(e.Entero(1), e.Entero(2))
        res = f.Fraccion(e.Entero(3), e.Entero(2))

        self.assertEqual(res, f1 + f2)

    def test_resta(self):
        """ a """
        f1 = f.Fraccion(e.Entero(2), e.Entero(2))
        f2 = f.Fraccion(e.Entero(1), e.Entero(2))

        res = f.Fraccion(e.Entero(1), e.Entero(2))
        self.assertEqual(res, f1 - f2)

    def test_multiplicacion(self):
        """ a """
        f1 = f.Fraccion(e.Entero(2), e.Entero(2))
        f2 = f.Fraccion(e.Entero(1), e.Entero(2))

        res = f.Fraccion(e.Entero(2), e.Entero(4))
        self.assertEqual(res, f1 * f2)

    def test_division(self):
        """ a """
        f1 = f.Fraccion(e.Entero(2), e.Entero(2))
        f2 = f.Fraccion(e.Entero(1), e.Entero(2))

        res = f.Fraccion(e.Entero(4), e.Entero(2))
        self.assertEqual(res, f1 / f2)

    def test_mayor_o_igual_retorna_verdadero_si_es_mayor(self):
        """ a """
        f1 = f.Fraccion(e.Entero(4), e.Entero(2))
        f2 = f.Fraccion(e.Entero(1), e.Entero(3))

        self.assertTrue(f1 >= f2)

    def test_mayor_o_igual_retorna_verdadero_si_es_igual(self):
        """ a """
        f1 = f.Fraccion(e.Entero(4), e.Entero(2))
        f2 = f.Fraccion(e.Entero(4), e.Entero(2))

        self.assertTrue(f1 >= f2)

    def test_mayor_o_igual_retorna_falso_si_es_menor(self):
        """ a """
        f1 = f.Fraccion(e.Entero(1), e.Entero(2))
        f2 = f.Fraccion(e.Entero(4), e.Entero(3))

        self.assertFalse(f1 >= f2)

    def test_menor_retorna_verdadero_si_es_menor(self):
        """ a """
        f1 = f.Fraccion(e.Entero(1), e.Entero(2))
        f2 = f.Fraccion(e.Entero(4), e.Entero(3))

        self.assertTrue(f1 < f2)

    def test_menor_retorna_falso_si_es_mayor(self):
        """ a """
        f1 = f.Fraccion(e.Entero(4), e.Entero(2))
        f2 = f.Fraccion(e.Entero(1), e.Entero(3))

        self.assertFalse(f1 < f2)

    def test_menor_retorna_falso_si_es_igual(self):
        """ a """
        f1 = f.Fraccion(e.Entero(4), e.Entero(2))
        f2 = f.Fraccion(e.Entero(4), e.Entero(2))

        self.assertFalse(f1 < f2)

    def test_division_entero_error(self):
        """ a """
        with self.assertRaises(ArithmeticError):
            f1 = f.Fraccion(e.Entero(1), e.Entero(2))
            f2 = f.Fraccion(e.Entero(1), e.Entero(4))

            f1 // f2 # type: ignore pylint: disable=pointless-statement

if __name__ == "__main__":
    unittest.main()
