""" Clases """

class RegistroAcademico():
    """ Registro académico """

    def __init__(self):
        self.__alumno = None #type: ignore pylint: skip-file
        self.__materia = None #type: ignore pylint: skip-file
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
    """ Clase que representa materias """

    def __init__(self, nombre, nota_minima, cuatrimestre, año):
        self.__nombre = nombre
        self.__nota_minima = nota_minima
        self.__cuatrimestre = cuatrimestre
        self.__año = año

    def nombre(self):
        """ Retorna nombre de la materia """

        return self.__nombre

    def nota_minima(self):
        """ Retorna nota """

        return self.__nota_minima

    def cuatrimestre(self):
        """ Retorna número de cuatrimestre """

        return self.__cuatrimestre

    def año(self): # pylint: disable=non-ascii-name

        """ Retorna año """

        return self.__año
