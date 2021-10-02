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
