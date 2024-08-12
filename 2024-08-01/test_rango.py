from entero import Entero
from fraccion import Fraccion, FraccionInvalidaError
from rango import Rango

import unittest

class TestMain(unittest.TestCase):
    def test_string(self):
        v1 = Entero(1)
        v2 = Entero(5)
        
        r1 = Rango(v1, v2)
        
        r1_string = r1.representar_en_string()
        
        self.assertEqual("[1, 5]", r1_string)
        
    def test_entero_dentro_de_limites(self):
        v1 = Entero(1)
        v2 = Entero(5)
        num = Entero(3)
        
        r1 = Rango(v1, v2)
        
        ans = r1.entero_dentro_de_limites(num)
    
    def test_tamaño_rango(self):
        v1 = Entero(1)
        v2 = Entero(8)

        r1 = Rango(v1, v2)
        
        ans = r1.tamaño_rango()
        
        self.assertEqual("7", ans)
        
    def test_esta_incluido_en(self):
        v1 = Entero(1)
        v2 = Entero(5)
        v3 = Entero(2)
        v4 = Entero(4)
        
        r1 = Rango(v1, v2)
        r2 = Rango(v3, v4)
        
        ans = r2.esta_incluido_en(r1)
        
        self.assertTrue(ans)
        
    def test_intersecta_con(self):
        v1 = Entero(1)
        v2 = Entero(5)
        v3 = Entero(3)
        v4 = Entero(7)
        
        r1 = Rango(v1, v2)
        r2 = Rango(v3, v4)
        
        ans = r1.intersecta_con(r2)
        
        self.assertTrue(ans)
        
if __name__ == "__main__":
    unittest.main()