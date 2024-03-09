numero = int(input("Ingrese un número entero: "))
suma_digitos = 0
while numero > 0:
    digito = numero % 10
    suma_digitos += digito
    numero //= 10  
print(f"La suma de los dígitos del número ingresado es: {suma_digitos}")
