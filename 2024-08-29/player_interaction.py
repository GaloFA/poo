# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, attribute-defined-outside-init, protected-access
""" Imports """
import game

class PlayerInteraction():
    """ Clase que maneja las interacciones con el usuario por terminal """
    def __init__(self):
        pass

    def play_again(self, game_instance: "game.Game"):
        """ Método que regunta si el usuario quiere seguir jugando """

        response = input("¿Quiere seguir jugando? (s/n): ").lower()

        while response not in ["s", "n"]:
            print("Respuesta inválida (s/n)")
            response = input("¿Quiere seguir jugando? (s/n): ").lower()

        if response == "s":
            game_instance.reset(game_instance._board.dimensions)
            return True

        return False

    def run_game(self):
        """ Ejecutar el juego """

        while True:
            try:
                dimensions = int(input("Ingrese las dimensiones del tablero: "))
                break

            except ValueError:
                print("Por favor, ingrese un número entero válido.")

        run_game = game.Game(dimensions)
        run_game.run()
