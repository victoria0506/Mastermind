from colored import fg, attr
class Tablero :
    def __init__(self) -> None:
        self.board = [[''] * 5 for _ in range(12)]
    def update(self, turnos, adivi, jugadas):
        for col in range(4) :
          self.board[turnos][col] = adivi[col]
        for col in range(4) :
            self.board[turnos][4] = jugadas[col]
        self.mostrar()
    def mostrar(self) :
        print("\nTablero")
        for row in self.board :
            display_tabla = ""
            for i in range(4) :
                color = row[i]
                display_tabla += f"{self.color_cir_adi(color)} "
            jugadas = row[4]
            display_tabla += f"{self.color_jugadas(jugadas)}"
            print(display_tabla)
    def color_cir_adi(self, color):
        colores = {'red': '🔴', 'blue': '🔵', 'green': '🟢', 'yellow': '🟡'}
        return colores.get(color, '⚪')
    def color_jugadas(self, jugadas) :
        colores = {'green': '🟢', 'orange': '🟠', 'white': '⚪'}
        return ''.join(colores.get(f, '⚪') for f in jugadas)