# Leer números hasta que se ingrese un negativo
while True:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        print("Se ingresó un número negativo, fin del programa.")
        break