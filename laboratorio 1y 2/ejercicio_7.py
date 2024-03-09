inicio_rango = int(input("Ingrese el número de inicio del rango: "))
fin_rango = int(input("Ingrese el número de fin del rango: "))
if inicio_rango > fin_rango:
    print("Error: El número de inicio debe ser menor o igual al número de fin.")
else:
    suma_pares = 0
    for numero in range(inicio_rango, fin_rango + 1):
        if numero % 2 == 0:
            suma_pares += numero

    print(f"La suma de los números pares en el rango [{inicio_rango}, {fin_rango}] es: {suma_pares}")
