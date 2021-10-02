import random

#dibujar tablero
def drawTable(table):
    print("   |   |")
    print(" " + table[7] + " | " + table[8] + " | " + table[9])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + table[4] + " | " + table[5] + " | " + table[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + table[1] + " | " + table[2] + " | " + table[3])
    print("   |   |")

#table = [" "]*10

#drawTable(table)

#preguntar que letra quiere ser el jugador
def askLetter():
    letra = 0
    while letra not in ["X", "O"]:
        letra = input("Que letra deseas ser: ").upper()

    if letra == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

#eleguir quien comienza
def whoFirst():
    if random.randint(0, 1) == 0:
        return "La computadora"
    else:
        return "El jugador"

#determinar si hay espacio libre en el tablero
def thereIsEmptySpace(tablero, jugada):

    return tablero[jugada] == " "

#elegir la jugada del jugador
def choosePlayUser(table):
    jugada = ""
    while jugada not in "1 2 3 4 5 6 7 8 9".split() or not thereIsEmptySpace(table, int(jugada)):
        jugada = input("Escribe tu jugada: ")

    return int(jugada)

#hacer la jugada
def makeGame(tablero, jugada, letra):
    tablero[jugada] = letra

#comprobar si ha ganado o ha perdido
def isWin(table, le):

    return ((table[7] == le and table[8] == le and table[9] == le) or
            (table[4] == le and table[5] == le and table[6] == le) or
            (table[1] == le and table[2] == le and table[3] == le) or
            (table[7] == le and table[4] == le and table[1] == le) or
            (table[8] == le and table[5] == le and table[2] == le) or
            (table[9] == le and table[6] == le and table[3] == le) or
            (table[7] == le and table[5] == le and table[3] == le) or
            (table[1] == le and table[5] == le and table[9] == le) )

#comprobar si el tablero esta lleno
def tableFull(tablero):

    for i in range(1, 10):
        if thereIsEmptySpace(tablero, i):
            return False
    return True

#crear una funcion que copie el tablero original
def copyTable(tablero):
    newTable = []
    for i in tablero:
        newTable.append(i)

    return newTable

#calcular la jugada en la esquina
def jugadaPosibleEsquina(tablero, lista):
    newList = []
    for i in lista:
        if thereIsEmptySpace(tablero, i):
            newList.append(i)

    if len(newList) != 0:
        return random.choice(newList)
    else:
        return None

#buscar a jugada para la computadora
def choosePlayerComputer(tablero, letraComputadora):

    if letraComputadora == "X":
        letraJugador = "O"
    else:
        letraJugador = "X"

    #hacer la jugada ganadora
    for i in range(1, 10):
        copia = copyTable(tablero)
        if thereIsEmptySpace(copia, i):
            makeGame(copia, i, letraComputadora)
            if isWin(copia, letraComputadora):
                return i

    #ver si el jugador hara la jugada ganadora y bloquearla
    for i in range(1, 10):
        copia = copyTable(tablero)
        if thereIsEmptySpace(copia, i):
            makeGame(copia, i, letraJugador)
            if isWin(copia, letraJugador):
                return i

    #jugar en las esquinas
    jugada = jugadaPosibleEsquina(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada

    #jugar en el centro
    if thereIsEmptySpace(tablero, 5):
        return 5

    #jugar en los lados laterales
    jugada = jugadaPosibleEsquina(tablero, [4, 6, 8, 2])
    if jugada != None:
        return jugada

#jugar de nuevo
def playAgain():
    print("Deseas jugar de nuevo ?")

    return input().upper().startswith("S")




#comenzar el juego

def main():

    while True:

        print("Bienvenido al Tateti")
        table = [" "] * 10
        letraJugador, letraComputadora = askLetter()
        turno  = whoFirst()
        print(turno, "irá primero")

        while True:

            if turno == "El jugador":
                drawTable(table)
                jugada = choosePlayUser(table)
                makeGame(table, jugada, letraJugador)

                if isWin(table, letraJugador):
                    drawTable(table)
                    print("Felicidades, Has ganado la partida!!")
                    break
                else:
                    if tableFull(table):
                        drawTable(table)
                        print("Ha sido un empate")
                        break
                    else:
                        turno = "La computadora"

            else:
                print("nada por el momento")
                jugada = choosePlayerComputer(table, letraComputadora)
                makeGame(table, jugada, letraComputadora)

                if isWin(table, letraComputadora):
                    drawTable(table)
                    print("Game over, la computadroa te ha ganado :(")
                    break
                else:
                    if tableFull(table):
                        drawTable(table)
                        print("Ha sido un empate")
                        break
                    else:
                        turno = "El jugador"

        print("\nFin del juego, Game Over\n")

        if not playAgain():
            break

main()
