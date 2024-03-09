def numeros_ordenados_mayor_a_menor(conjunto_numeros):
    conjunto_ordenado = sorted(conjunto_numeros, reverse=True)
    return conjunto_ordenado

conjunto = {5, 2, 8, 1, 9}
conjunto_ordenado = numeros_ordenados_mayor_a_menor(conjunto)

print("Números ordenados de mayor a menor:", conjunto_ordenado)
