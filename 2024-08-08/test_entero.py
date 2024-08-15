""" a """

import unittest
import entero as e
import fraccion as f

class TestEntero(unittest.TestCase):
    """ a """

    def test_str(self):
        """ a """
        entero = e.Entero(5)
        self.assertEqual("5", str(entero))

    def test_repr(self):
        """ a """
        entero = e.Entero(5)
        self.assertEqual("e.Entero(5)", repr(entero))

    def test_eq_retorna_true_para_dos_numeros_iguales(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(1)

        self.assertTrue(e1 == e2)

    def test_eq_retorna_false_para_dos_numeros_distintos(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)

        self.assertFalse(e1 == e2)

    def test_suma(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)

        res = e.Entero(3)
        self.assertEqual(res, e1 + e2)

    def test_resta(self):
        """ a """
        e1 = e.Entero(2)
        e2 = e.Entero(1)

        self.assertEqual(e.Entero(1), e1 - e2)

    def test_multiplicacion(self):
        """ a """
        e1 = e.Entero(2)
        e2 = e.Entero(3)

        self.assertEqual(e.Entero(6), e1 * e2)

    def test_division_sin_resto(self):
        """ a """
        e1 = e.Entero(6)
        e2 = e.Entero(3)

        self.assertEqual(e.Entero(2), e1 / e2)

    def test_dividir_con_resto_da_resultado_fraccion(self):
        """ a """
        e1 = e.Entero(5)
        e2 = e.Entero(2)
        ans = e1 / e2 # type: ignore

        self.assertEqual(f.Fraccion(e1, e2), ans)

    def test_dividir_por_cero_levanta_error(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(0)

        with self.assertRaises(ZeroDivisionError):
            e1 / e2  # type: ignore pylint: disable=pointless-statement

    def test_division_entera_sin_resto(self):
        """ a """
        e1 = e.Entero(6)
        e2 = e.Entero(3)

        self.assertEqual(e.Entero(2), e1 // e2)

    def test_division_entera_con_resto_ignora_el_resto(self):
        """ a """
        e1 = e.Entero(7)
        e2 = e.Entero(3)

        self.assertEqual(e.Entero(2), e1 // e2)

    def test_mayor_o_igual_retorna_verdadero_si_es_mayor(self):
        """ a """
        e1 = e.Entero(2)
        e2 = e.Entero(1)

        self.assertTrue(e1 >= e2)

    def test_mayor_o_igual_retorna_verdadero_si_es_igual(self):
        """ a """
        e1 = e.Entero(2)
        e2 = e.Entero(2)

        self.assertTrue(e1 >= e2)

    def test_mayor_o_igual_retorna_falso_si_es_menor(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)

        self.assertFalse(e1 >= e2)

    def test_menor_retorna_verdadero_si_es_menor(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)

        self.assertTrue(e1 < e2)

    def test_menor_retorna_falso_si_es_igual(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(1)

        self.assertFalse(e1 < e2)

    def test_menor_retorna_falso_si_es_mayor(self):
        """ a """
        e1 = e.Entero(2)
        e2 = e.Entero(1)

        self.assertFalse(e1 < e2)


if __name__ == "__main__":
    unittest.main()
