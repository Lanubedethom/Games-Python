'''
#calcular la suma de los n primeros numeros

numero = int(input("ingresa el n-esimo numero a suma: "))

suma = 0
k = 1
while numero <= 0:
    numero = int(input("prohibido numeros negativos: "))

while k <= numero:
    suma = suma + k
    k += 1

print(f"la suma termina en {suma}")

#algoritmo para determinar si la temperatura para dies dias

dia  = 0
diasSinHelada = 0
diasConHelada = 0

while dia < 10:
    temperature = float(input(f"ingrese temperatura para dia {dia + 19}: "))
    while (temperature < -7.3 or temperature > 3.9):
        temperature = float(input("ingrese la temperatura dentro del parametro: "))

    if temperature <= 0:
        diasConHelada += 1
    else:
        diasSinHelada += 1

    dia += 1

print("numero de dias con helada: ", diasConHelada)
print("el numero de dias si helada: ", diasSinHelada)

#sumar las fracciones , solo eso
print("algorimto que calcula la suma de una fraccion")
input("presiona enter para calcular")

suma = 0
i = 0

num = 1
dem = 100

while i < 100:
    suma = suma + (num + i)/(dem - i)

    i += 1

print("la suma total seria", suma)

#algirmo para calcular la suma de una serie aritmetica elevado al exponente y con signos alternos

suma = 0
i = 1
signo = 1
while i <= 100:
    suma = suma + signo*i**2
    i += 1
    signo = -signo

print("la suma total seria: ", suma) '''

#calcular el MCD de dos numeros enteros

number1 = int(input("ingrse numero 1: "))
while number1 <= 0:
    number1 = int(input("ingrese numeros no negativos: "))
number2 = int(input("ingrese numero 2: "))
while number2 <= 0:
    number2 = int(input("ingrese numeros negativos: "))

resto = number1 % number2

while resto != 0:
    number1 = number2
    number2 = resto
    resto = number1 % number2

MCD = number2

print("el MCD es: ", MCD)
