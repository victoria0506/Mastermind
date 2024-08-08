from colored import fg, attr

class Tablero:
    def __init__(self) -> None:
        self.board = [[''] * 5 for _ in range(12)]
    
    def update(self, turnos, adivi, jugadas):
        for col in range(4):
            self.board[turnos][col] = adivi[col]
        self.board[turnos][4] = jugadas
        self.mostrar()

    def mostrar(self):
        print("\nTablero")
        print("Color green es que el color esta correcto y en posicion correcta, Orange es que le color se encuentra pero no esta en la posicion correcto")
        for row in self.board:
            display_tabla = ""
            for i in range(4):
                color = row[i]
                display_tabla += f"{self.color_cir_adi(color)} "
            display_tabla += f"{self.color_jugadas(row[4])}"
            print(display_tabla)

    def color_cir_adi(self, color):
        colores = {'red': '🔴', 'blue': '🔵', 'green': '🟢', 'yellow': '🟡'}
        return colores.get(color, '⚪')  
    def color_jugadas(self, jugadas):
        emojis = {'green': '🟢', 'orange': '🟠', 'white': '⚪'}
        return ''.join(emojis.get(f, '⚪') for f in jugadas)
