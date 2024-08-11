from entero import Entero
from fraccion import Fraccion
from numero import Numero
import unittest


class TestNumero(unittest.TestCase):
    def test_dividir_dos_enteros_da_fraccion_cuando_el_dividendo_no_es_multiplo_del_divisor(self):
        e1 = Entero(1)
        e2 = Entero(2)
        
        res = Fraccion(Entero(1), Entero(2))
        self.assertEqual(res, e1 / e2)
    
    def test_suma_entero_fraccion(self):
        e1 = Entero(2)
        e2 = Entero(1)
        e3 = Entero(2)
        f1 = Fraccion(e2, e3)
        
        ans = e1 + f1

        self.assertEqual(Fraccion(Entero(5), Entero(2)), ans)

    def test_suma_entero_fraccion_da_entero_si_denominador_es_divisor_del_entero(self):
        e1 = Entero(1)
        e2 = Entero(2)
        f1 = Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)
    
    def test_suma_entero_fraccion_da_fraccion_si_denominador_no_es_divisor_del_entero(self):
        e1 = Entero(1)
        e2 = Entero(3)
        f1 = Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)

    def test_suma_fraccion_entero_da_entero_si_denominador_es_divisor_del_entero(self):
        e1 = Entero(1)
        e2 = Entero(2)
        f1 = Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)
    
    def test_suma_fraccion_entero_da_fraccion_si_denominador_no_es_divisor_del_entero(self):
        e1 = Entero(1)
        e2 = Entero(3)
        f1 = Fraccion(e1, e2)

        ans = e2 * f1

        self.assertEqual(e1, ans)
        
if __name__ == "__main__":
    unittest.main()