"""a """

class RegistroAcademico():
    """ Registro académico """

    def __init__(self):
        self.__alumno = None
        self.__materia = None
        self.__alumnos_cursando_materias = {}

    def agregar_alumno_a_materia(self, alumno, materia):
        """ Agrega a un alumno a la materia """
        if alumno not in self.__alumnos_cursando_materias:
            self.__alumnos_cursando_materias[alumno] = []

        self.__alumnos_cursando_materias[alumno].append(materia)

    def alumno_cursa_materia(self, alumno, materia) -> bool:
        """ Retorna si el alumno cursa una materia (bool) """
        return materia in self.__alumnos_cursando_materias[alumno]

class Alumno():
    """ Clase que representa alumnos """
    def __init__(self, dni):
        self.__dni = dni

    def dni(self):
        """ Retorna el dni del alumno """
        return self.__dni

class Materia():

    def __init__(self, nombre, nota):
        self.__nombre = nombre
        self.__nota = nota

    def nombre(self):
        return self.__nombre

    def nota(self):
        return self.__nota