import random
import sys

#Modulo que sirve para dibujar el oceano
def dibujarTablero(tab):
    lineaH = "    "
    for i in range(1, 6):
        lineaH += (" "*9) + str(i)
    print(lineaH)
    print("   " + ("0123456789"*6))
    print()
    #imprimir un rango de 15 filas
    for i in range(15):
        if i in range(10):
            espacioExtra = " "
        else:
            espacioExtra = ""
        print("%s%s %s %s" %(espacioExtra, i, obtenerFila(tab, i), i))
    print()
    print("   " + ("0123456789"*6))
    print(lineaH)

#modulo que determina nuevo tablero
def obtenerNuevoTablero():
    tablero = []
    for i in range(15):
        tablero.append([])
        for j in range(60):
            if random.randint(0, 1) == 0:
                tablero[i].append("~")
            else:
                tablero[i].append("`")

    return tablero

#determinar fila de oceano
def obtenerFila(tablero, fila):
    filaTablero = ""
    for i in range(60):
        filaTablero += tablero[fila][i]

    return filaTablero

#cofres aleatorios
def obtenerCofresAleatorios(numCofres):
    cofres = []

    for i in range(numCofres):
        cofres.append([random.randint(0, 14), random.randint(0, 59)])

    return cofres

cofres = obtenerCofresAleatorios(3)
print(cofres)
