def numeros_no_duplicados(conjunto_numeros):
    numeros_vistos = set()
    duplicados = set()
    for numero in conjunto_numeros:
        if numero in numeros_vistos:
            duplicados.add(numero)
        else:
            numeros_vistos.add(numero)

    numeros_no_duplicados = set(conjunto_numeros) - duplicados

    return numeros_no_duplicados

conjunto_numeros = [1, 2, 3, 2, 4, 5, 3, 6]
conjunto_no_duplicados = numeros_no_duplicados(conjunto_numeros)

print("Conjunto original:", conjunto_numeros)
print("Conjunto de números no duplicados:", conjunto_no_duplicados)
