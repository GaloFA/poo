""" Clases """

class Juego():
    """ Clase que se encarga de correr el juego """
    def __init__(self):
        pass

    def run(self):
        """ Método que representa al juego ejecutándose """

        running = True
        partida_terminada = True # hardcodeo temporal
        quiere_continuar = False # hardcodeo temporal

        while running:
            if partida_terminada and not quiere_continuar:
                running = False
