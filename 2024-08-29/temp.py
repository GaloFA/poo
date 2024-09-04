# pylint: skip-file
from game import Game

def main():
    while True:
        try:
            dimensions = int(input("Ingrese las dimensiones del tablero: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    game = Game(dimensions)
    game.run()

main()