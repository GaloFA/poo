# pylint: skip-file
import unittest
from entero import Entero
from fraccion import Fraccion

class TestEntero(unittest.TestCase):   

    def test_str(self):
        
        e1 = Entero(5)
        self.assertEqual("5", str(e1))

    def test_repr(self):
        
        e1 = Entero(5)
        self.assertEqual("Entero(5)", repr(e1))

    def test_eq_retorna_true_para_dos_numeros_iguales(self):
        
        e1 = Entero(1)
        e2 = Entero(1)

        self.assertTrue(e1 == e2)

    def test_eq_retorna_false_para_dos_numeros_distintos(self):
        
        e1 = Entero(1)
        e2 = Entero(2)

        self.assertFalse(e1 == e2)

    def test_suma(self):
        
        e1 = Entero(1)
        e2 = Entero(2)

        res = Entero(3)
        self.assertEqual(res, e1 + e2)

    def test_resta(self):
        
        e1 = Entero(2)
        e2 = Entero(1)

        self.assertEqual(Entero(1), e1 - e2)

    def test_multiplicacion(self):
        
        e1 = Entero(2)
        e2 = Entero(3)

        self.assertEqual(Entero(6), e1 * e2)

    def test_division_sin_resto(self):
        
        e1 = Entero(6)
        e2 = Entero(3)

        self.assertEqual(Entero(2), e1 / e2)

    def test_dividir_con_resto_da_resultado_fraccion(self):
        
        e1 = Entero(5)
        e2 = Entero(2)
        ans = e1 / e2 # type: ignore

        self.assertEqual(Fraccion(e1, e2), ans)

    def test_dividir_por_cero_levanta_error(self):
        
        e1 = Entero(1)
        e2 = Entero(0)

        with self.assertRaises(ZeroDivisionError):
            e1 / e2  # type: ignore pylint: disable=pointless-statement

    def test_division_entera_sin_resto(self):
        
        e1 = Entero(6)
        e2 = Entero(3)

        self.assertEqual(Entero(2), e1 // e2)

    def test_division_entera_con_resto_ignora_el_resto(self):
        
        e1 = Entero(7)
        e2 = Entero(3)

        self.assertEqual(Entero(2), e1 // e2)

    def test_mayor_o_igual_retorna_verdadero_si_es_mayor(self):
        
        e1 = Entero(2)
        e2 = Entero(1)

        self.assertTrue(e1 >= e2)

    def test_mayor_o_igual_retorna_verdadero_si_es_igual(self):
        
        e1 = Entero(2)
        e2 = Entero(2)

        self.assertTrue(e1 >= e2)

    def test_mayor_o_igual_retorna_falso_si_es_menor(self):
        
        e1 = Entero(1)
        e2 = Entero(2)

        self.assertFalse(e1 >= e2)

    def test_menor_retorna_verdadero_si_es_menor(self):
        
        e1 = Entero(1)
        e2 = Entero(2)

        self.assertTrue(e1 < e2)

    def test_menor_retorna_falso_si_es_igual(self):
        
        e1 = Entero(1)
        e2 = Entero(1)

        self.assertFalse(e1 < e2)

    def test_menor_retorna_falso_si_es_mayor(self):
        
        e1 = Entero(2)
        e2 = Entero(1)

        self.assertFalse(e1 < e2)


if __name__ == "__main__":
    unittest.main()
