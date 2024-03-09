def numeros_ordenados(conjunto_numeros):
    conjunto_ordenado = sorted(conjunto_numeros)
    nuevo_conjunto = set(conjunto_ordenado)
    return nuevo_conjunto

conjunto = {5, 2, 8, 1, 9}
conjunto_ordenado = numeros_ordenados(conjunto)

print("Números ordenados de menor a mayor:", conjunto_ordenado)
