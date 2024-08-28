# pylint: skip-file
import unittest
from colecciones import IteradorDeColeccion, ContenedorIterable, ContenedorIterable2


class TestColecciones(unittest.TestCase):

    def test_01_elemento_esperado_iterador(self):

        contenedor = ContenedorIterable2()
        contenedor.agregar(5, 1)
        contenedor.agregar(3, 1)
        contenedor.agregar(4, 2)
        contenedor.agregar(8, 1)
        contenedor.agregar(10, 2)

        elementos_esperados = [5, 3, 8, 4, 10]
        resultado_elementos = []
        iterador = iter(contenedor)
        
        for i in range(len(elementos_esperados)):
            resultado_elementos.append(next(iterador))

            self.assertEqual(resultado_elementos[i], elementos_esperados[i])

    def test_02_elemento_esperado_generador(self):

        contenedor = ContenedorIterable2()
        contenedor.agregar(5, 1)
        contenedor.agregar(3, 1)
        contenedor.agregar(4, 2)
        contenedor.agregar(8, 1)
        contenedor.agregar(10, 2)

        elementos_esperados = [5, 3, 8, 4, 10]
        resultado_elementos = []
        iterador = iter(contenedor)
        
        for i in range(len(elementos_esperados)):
            resultado_elementos.append(next(iterador))

            self.assertEqual(resultado_elementos[i], elementos_esperados[i])

if __name__ == "__main__":
    unittest.main()
