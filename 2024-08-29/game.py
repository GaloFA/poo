""" Imports """

class Game():
    """ Clase que se encarga de correr el juego """
    def __init__(self):
        pass

    def run(self):
        """ Método que representa al juego ejecutándose """

        running = True
        match_finished = True # hardcodeo temporal
        continues = False # hardcodeo temporal

        while running:
            if match_finished and not continues:
                running = False
