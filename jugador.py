from tablero import Tablero
import random
class Jugador_creador:
    def __init__(self, code, turnos_max, board) -> None:
        self.code = code
        self.turnos_max = turnos_max
        self.board = board
    def jugar(self):
        for turnos in range(self.turnos_max) :
            adivi = input(f"turnos {turnos+1}. Introduzca su adivinanza (Ejemplo : red , blue, geen, yellow) ").strip().split()
            jugadas= self.obten_juga(adivi)
            self.board(turnos, adivi, jugadas)
            if jugadas == ["green", "green", "green", "green"] :
                print("¡Has adivinado el código secreto!")
                break
        else :
            print(f"No adivinaste el código secreto. El código era:", ' '.join(self.code))
    def obten_juga(self, adi):
        jugadas = []
        codi_copia = self.code[:]
        codi_adi = adi[:]
        for i in range(4) :
            if adi[i] == self.code[i] :
                jugadas.append("green")
                codi_copia[i] == None
                codi_adi[i] == "matched"
        for i in range(4):
            if codi_copia != "matched" :
                if codi_adi[i] in codi_copia :
                    jugadas.append("orange")
        while len(jugadas) < 4:
            jugadas.append("white")
        return jugadas
    
    
    
    
class Jugador_adivinador():
    def __init__(self, code, turnos_max, board) -> None:
        self.code = code
        self.turnos_max = turnos_max
        self.board = board
        self.colores = ["red", "blue", "yellow", "green"]
    def jugar(self) :
        print(self.turnos_max)
        for turnos in range(self.turnos_max) :
            adivi = self.hacer_adi()
            jugadas = self.obte_juga(adivi)
            print(jugadas)
            self.board(turnos, adivi, jugadas)
            if jugadas == ["green", "green", "green", "green"] :
                print("¡La computadora ha adivinado el código secreto!")
                break
        else:
            print("La computadora no adivinó el código secreto. El código era:", ' '.join(self.code))
    def hacer_adi(self):
        return [random.choice(self.colores) for _ in range(4)]
    def obte_juga(self, adi) :
        jugadas = []
        codi_copia = self.code[:]
        codi_adi = adi[:]
        for i in range(4) :
            if adi[i] == self.code[i] :
                jugadas.append("green")
                codi_copia[i] == None
                codi_adi[i] == "matched"
        for i in range(4):
            if codi_copia != "matched" :
                if codi_adi[i] in codi_copia :
                    jugadas.append("orange")
        while len(jugadas) < 4:
            jugadas.append("white")
        return jugadas
