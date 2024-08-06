

class Tablero() :
    def __init__(self) -> None:
        self.tabla = [[''] * 5 for _ in range(12)]
        
    def update(self, turnos, adivi, jugadas):
        for col in range(4) :
          self.tabla[turnos][col] = adivi[col]
        for col in range(4) :
            self.tabla[turnos][col] = jugadas[col]
            
    def mostrar(self) :
        print("\nTablero")
        for row in self.tabla :
            display_tabla = " "
            for i in range(4) :
                color = row[i]
                