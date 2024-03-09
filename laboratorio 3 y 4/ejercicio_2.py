def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n - 1)
numero = 5
resultado = suma(numero)
print("La suma de los números del 1 al",numero,"es:", resultado)
