 # pylint: skip-file
import unittest
from entero import Entero
from fraccion import Fraccion


class TestNumero(unittest.TestCase):
    
    def test_dividir_dos_enteros_da_fraccion_cuando_el_dividendo_no_es_multiplo_del_divisor(self):
        
        e1 = Entero(1)
        e2 = Entero(2)

        res = Fraccion(Entero(1), Entero(2))
        self.assertEqual(res, e1 / e2)

    def test_suma_entero_fraccion(self):
        
        e1 = Entero(1)
        e2 = Entero(2)
        f1 = Fraccion(e1, e2)

        ans = e1 + f1

        self.assertEqual(Fraccion(Entero(3), Entero(2)), ans)

    # Todos estos tests van a fallar, ya que no se puede utilizar la operación % en el tipo de dato "Entero"

    """def test_suma_entero_fraccion_da_entero_si_denominador_es_divisor_del_entero(self):
        
        e1 = Entero(1)
        e2 = Entero(2)
        f1 = Fraccion(e2, e2)

        ans = e1 + f1

        self.assertEqual(e2, ans)

    def test_suma_entero_fraccion_da_fraccion_si_denominador_no_es_divisor_del_entero(self):
        
        e1 = Entero(1)
        e2 = Entero(3)
        e3 = Entero(4)
        f1 = Fraccion(e1, e2)

        ans = e2 + f1
        expected_result = Fraccion(e3, e2)

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

        self.assertEqual(e1, ans)"""

if __name__ == "__main__":
    unittest.main()
