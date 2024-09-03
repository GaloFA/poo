#type: ignore pylint: skip-file
from entero import Entero
import unittest

class TestMain(unittest.TestCase):
    def test_string(self):
        v1 = Entero(1)

        v1_str = v1.valor_string()

        self.assertEqual("1", v1_str)

    def test_suma(self):
        v1 = Entero(1)
        v2 = Entero(2)

        ans = v1.suma(v2)
        ans_str = ans.valor_string()

        self.assertEqual("3", ans_str)

    def test_resta(self):
        v1 = Entero(3)
        v2 = Entero(2)

        ans = v1.resta(v2)
        ans_str = ans.valor_string()

        self.assertEqual("1", ans_str)

    def test_multiplicacion(self):
        v1 = Entero(3)
        v2 = Entero(4)

        ans = v1.multiplicacion(v2)
        ans_str = ans.valor_string()

        self.assertEqual("12", ans_str)

    def test_division(self):
        v1 = Entero(12)
        v2 = Entero(3)

        ans = v1.division(v2)
        ans_str = ans.valor_string()

        self.assertEqual("4", ans_str)

    def test_mayor(self):
        v1 = Entero(5)
        v2 = Entero(3)

        ans = v1.mayor(v2)

        self.assertTrue(ans)

    def test_mayor_igual(self):
        v1 = Entero(5)
        v2 = Entero(5)

        ans = v1.mayor_igual(v2)

        self.assertTrue(ans)

    def test_menor(self):
        v1 = Entero(2)
        v2 = Entero(3)

        ans = v1.menor(v2)

        self.assertTrue(ans)

    def test_menor_igual(self):
        v1 = Entero(4)
        v2 = Entero(4)

        ans = v1.menor_igual(v2)

        self.assertTrue(ans)

    def test_negativo(self):
        v1 = Entero(-1)

        ans = v1.negativo()

        self.assertTrue(ans)

    def test_positivo(self):
        v1 = Entero(1)

        ans = v1.positivo()

        self.assertTrue(ans)

    def test_igual_a_cero(self):
        v1 = Entero(0)

        ans = v1.igual_a_cero()

        self.assertTrue(ans)

if __name__ == "__main__":
    unittest.main()