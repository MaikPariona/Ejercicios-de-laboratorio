def encontrar_duplicados(conjunto_numeros):
    duplicados = set()
    numeros_vistos = set()
    for numero in conjunto_numeros:
        if numero in numeros_vistos:
            duplicados.add(numero)
        else:
            numeros_vistos.add(numero)

    return duplicados

conjunto_numeros = [1, 2, 3, 2, 4, 5, 3, 6]
conjunto_duplicados = encontrar_duplicados(conjunto_numeros)

print("Conjunto original:", conjunto_numeros)
print("Conjunto de números duplicados:", conjunto_duplicados)
