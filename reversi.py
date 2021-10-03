import random, sys

def dibujarTablero(tablero):

    lineaH = "  +---+---+---+---+---+---+---+---+"
    lineaV = "  |   |   |   |   |   |   |   |   |"
    number = "    1   2   3   4   5   6   7   8"

    print(number)
    print(lineaH)
    for y in range(8):
        print(lineaV)
        print(y+1, end="")
        for x in range(8):
            print(" | %s" %(tablero[x][y]), end="")
        print(" |")
        print(lineaV)
        print(lineaH)


def crearTablero():
    tablero = []
    for i in range(8):
        tablero.append([" "]*8)
    return tablero

#actualizar tablero por defecto
def actualizarTablero(tablero):
    for x in range(8):
        for y in range(8):
            tablero[x][y] = " "

    tablero[3][3] = "X"
    tablero[4][3] = "O"
    tablero[3][4] = "O"
    tablero[4][4] = "X"

#eligir badosa
def elegirBaldosa():
    baldosa = ""
    while baldosa not in ("X", "O"):
        print("que baldosa desear ser: ")
        baldosa = input().upper()

    if baldosa == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

#funcion que calcula el puntaje
def contarPuntaje(table):
    puntajeX = 0
    puntajeY = 0
    for x in range(8):
        for y in range(8):
            if table[x][y] == "X":
                puntajeX += 1
            if table[x][y] == "O":
                puntajeY += 1
    return {"X":puntajeX, "O":puntajeY}

#funcion que imprime el puntaje
def mostrarPuntaje(talePlayer, taleComputador, newTable):
    puntaje = contarPuntaje(newTable)
    print(f"El jugador tiene: {puntaje[talePlayer]} puntos")
    print(f"La computadora tiene: {puntaje[taleComputador]} puntos")

#funcio que elige un jugada
def eligirJugada():

    cifra18 = "1 2 3 4 5 6 7 8".split()
    while True:
        print("Elige una coordenada para el juego.")
        print("escribe 'salir' si deseas salir")
        print("escribe 'pistas' si deseas alguna ayuda")}

        jugada = input().lower()

        if jugada == "salir":
            return "salir"
        if jugada == "pistas":
            return "pistas"
        if len(jugada) == 2 and (jugada[0] in cifra18) and (jugada[1] in cifra18):
            x = int(jugada[0]) - 1
            y = int(jugada[1]) - 1

            if esJugadaValida(tablero, baldosa, talePlayer, taleComputador) == False:
                continue
            else:
                break
        else:
            print("los valores que ingresastes no estan dentro del parametro. Intenta de nuevo")

    return [x, y]



#quien jugara primero
def quienPrimero():
    if random.randint(0, 1) == 0:
        return "La computadora"
    else:
        return "El jugador"

def main():

    newTable = crearTablero()
    actualizarTablero(newTable)
    talePlayer, taleComputador = elegirBaldosa()
    turno = quienPrimero()
    #turno = "El jugador"
    print(turno, " irá primero")

    if turno == "El jugador":
        dibujarTablero(newTable)
        mostrarPuntaje(talePlayer, taleComputador, newTable)

    #es solo una muestra para git
    else:
        print("la computadora ira primero")
        dibujarTablero(newTable)
        mostrarPuntaje(taleComputador, talePlayer, newTable)

    #otro muestra para git
    if endGame():
        break
        #otro ejemplo para entender ramas
        print("este es un ejemplo para entender ramas, ok no")




#main()
