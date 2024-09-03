#type: ignore pylint: skip-file
from entero import Entero
from fraccion import Fraccion, FraccionInvalidaError

import unittest

class TestMain(unittest.TestCase):
    def test_string(self):
        v1 = Entero(1)
        v2 = Entero(2)
        f1 = Fraccion(v1, v2)
        f1_str = f1.valor_fraccion()
        self.assertEqual("1/2", f1_str)
        
    def test_denominador_cero(self):
        v1 = Entero(1)
        v2 = Entero(0)
        
        with self.assertRaises(FraccionInvalidaError):
            Fraccion(v1, v2)
    
    def test_divisor_comun_maximo(self):
        v1 = Entero(25)
        v2 = Entero(50)
        f = Fraccion(v1, v2)
        
        dcm = f.calcular_divisor_comun_maximo(v1, v2)
        
        self.assertEqual(25, dcm)

    def test_simplificacion(self):
        v1 = Entero(25)
        v2 = Entero(50)
        f = Fraccion(v1, v2)
        
        ans = f.simplificar_fraccion()
        
        self.assertEqual("1/2", ans)
        
    def test_equivalencia_de_fracciones(self):
        v1 = Entero(6)
        v2 = Entero(4)
        v3 = Entero(12)
        v4 = Entero(8)
        
        f1 = Fraccion(v1, v2)
        f2 = Fraccion(v3, v4)
        
        self.assertTrue(f1.equivalencia_de_fracciones(f1, f2))
    
    
    def test_sumar_fracciones(self):
        v1 = Entero(1)
        v2 = Entero(2)
        v3 = Entero(1)
        v4 = Entero(3)
        
        f1 = Fraccion(v1, v2)
        f2 = Fraccion(v3, v4)
        
        ans = f1.sumar_fracciones(f2)
        
        self.assertEqual("5/6", ans)

    def test_restar_fracciones(self):
        v1 = Entero(1)
        v2 = Entero(2)
        v3 = Entero(1)
        v4 = Entero(3)
        
        f1 = Fraccion(v1, v2)
        f2 = Fraccion(v3, v4)
        
        ans = f1.restar_fracciones(f2)
        
        self.assertEqual("1/6", ans)

    def test_multiplicar_fracciones(self):
        v1 = Entero(1)
        v2 = Entero(2)
        v3 = Entero(2)
        v4 = Entero(3)
        
        f1 = Fraccion(v1, v2)
        f2 = Fraccion(v3, v4)
        
        ans = f1.multiplicar_fracciones(f2)
        
        self.assertEqual("1/3", ans)

    def test_dividir_fracciones(self):
        v1 = Entero(1)
        v2 = Entero(2)
        v3 = Entero(2)
        v4 = Entero(3)
        
        f1 = Fraccion(v1, v2)
        f2 = Fraccion(v3, v4)
        
        ans = f1.dividir_fracciones(f2)
        
        self.assertEqual("3/4", ans)
    
if __name__ == "__main__":
    unittest.main()