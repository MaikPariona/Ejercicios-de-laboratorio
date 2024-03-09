def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados = sorted(conjunto_numeros)
    return set(numeros_ordenados)


conjunto_numeros = {5, 3, 8, 2, 3, 10, 5}
numeros_ordenados_sin_duplicados = numeros_ordenados_sin_duplicados(conjunto_numeros)

print("Conjunto original de números:", conjunto_numeros)
print("Números ordenados sin duplicados:", numeros_ordenados_sin_duplicados)
