""" a """
import unittest
import entero as e
import fraccion as f


class TestNumero(unittest.TestCase):
    """ a """
    def test_dividir_dos_enteros_da_fraccion_cuando_el_dividendo_no_es_multiplo_del_divisor(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)

        res = f.Fraccion(e.Entero(1), e.Entero(2))
        self.assertEqual(res, e1 / e2)

    def test_suma_entero_fraccion(self):
        """ a """
        e1 = e.Entero(2)
        e2 = e.Entero(1)
        e3 = e.Entero(2)
        f1 = f.Fraccion(e2, e3)

        ans = e1 + f1

        self.assertEqual(f.Fraccion(e.Entero(5), e.Entero(2)), ans)

    def test_suma_entero_fraccion_da_entero_si_denominador_es_divisor_del_entero(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)
        f1 = f.Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)

    def test_suma_entero_fraccion_da_fraccion_si_denominador_no_es_divisor_del_entero(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(3)
        f1 = f.Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)

    def test_suma_fraccion_entero_da_entero_si_denominador_es_divisor_del_entero(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(2)
        f1 = f.Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)

    def test_suma_fraccion_entero_da_fraccion_si_denominador_no_es_divisor_del_entero(self):
        """ a """
        e1 = e.Entero(1)
        e2 = e.Entero(3)
        f1 = f.Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)

if __name__ == "__main__":
    unittest.main()
