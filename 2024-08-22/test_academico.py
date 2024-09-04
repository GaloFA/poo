# pylint: skip-file
import unittest

from academico import RegistroAcademico, Alumno, Materia

class TestRegistroAcademico(unittest.TestCase):
    def setUp(self) -> None:
        self.registro = RegistroAcademico()
        self.alumno = Alumno(1234)
        self.materia_matematica = Materia("Matemática") #type: ignore pylint: skip-file

    
    #def test_01_constructor(self):
        #registro = RegistroAcademico()

    #def test_02_agregar_alumno_a_materia(self):
        #registro = RegistroAcademico()
        #alumno = Alumno(1234)
        #materia = Materia("Matemática") #type: ignore pylint: skip-file

        #registro.agregar_alumno_a_materia(alumno, materia)
        
        #self.assertTrue(registro.alumno_cursa_materia(alumno, materia))

class TestAlumno(unittest.TestCase):
    def test_01_constructor(self):
        dni = 123123
        alumno = Alumno(dni)
        
        self.assertEqual(dni, alumno.dni())

#class TestMateria(unittest.TestCase):
    #def