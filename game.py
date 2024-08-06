
import random

class Game :
    def __init__(self) -> None:
        self.max_turn = 12
        
    def inicio(self) :
        opcion = input("desea ser el creador del juego (C) o adivinador (A) ")
        if opcion == "c" :
            print("sera creador")
            self.crear_codigo()
        else :
            self.random_codigo()
            
    def crear_codigo(self) :
        print("Introduce el código secreto de 4 colores. Los colores disponibles son: red, blue, green, yellow.")
        while True :
            codigo = input("Codigo (ejemplo :red, blue, green, yellow) ").strip().split()
            if len(codigo) == 4 :
                return codigo
            else :
                print("Codigo invalido, asegurate de que sean 4 colores ")
    def random_codigo(self) :
        self.colors = ["red", "blue", "greed", "yellow"]
        return [random.choice(self.colors) for i in range(4)]

jugador = Game()
jugador.inicio()