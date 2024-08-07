
import random
from jugador import Jugador_adivinador
from jugador import Jugador_creador
from tablero import Tablero

class Game :
    def __init__(self):
        self.turnos_max = 12
        self.board = Tablero()
        self.code = None
    def inicio(self) :
        opcion = input("desea ser el creador del juego (C) o adivinador (A) ")
        if opcion == "c" :
            self.code = self.crear_codigo()
            self.jugador_creador()
        elif opcion == "a":
            self.code = self.random_codigo()
            self.jugador_adivinador()
        else :
            print("Opcion invalida, porfavor eliga C o A ")
            self.inicio()
    def crear_codigo(self) :
        print("Introduce el código secreto de 4 colores. Los colores disponibles son: red, blue, green, yellow.")
        while True :
            code = input("Codigo (ejemplo :red, blue, green, yellow) ").strip().split()
            if len(code) == 4  :
                return code
            else :
               print("Codigo invalido, asegurate de que sean 4 colores ")
    def random_codigo(self) :
        self.colors = ["red", "blue", "greed", "yellow"]
        return [random.choice(self.colors) for i in range(4)]
    def jugador_creador(self) :
        creador = Jugador_adivinador(self.code, self.turnos_max ,self.board.update)
        creador.jugar()
    def jugador_adivinador(self):
        adivinador = Jugador_creador(self.code, self.turnos_max,self.board.update)
        adivinador.jugar()
     
if __name__ == "__main__":
    Game().inicio()