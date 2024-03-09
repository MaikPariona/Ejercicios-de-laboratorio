def palabras_palindromos_ordenadas(conjunto_palabras):
    palindromos_ordenados = set()

    for palabra in conjunto_palabras:
        palabra_sin_espacios = ''.join(palabra.lower().split())
        if palabra_sin_espacios == palabra_sin_espacios[::-1]:
            palindromos_ordenados.add(palabra)

    palindromos_ordenados = sorted(palindromos_ordenados, key=len)

    return palindromos_ordenados

conjunto_palabras = {"asno", "level", "civic", "python", "Ana lava lana"}
palindromos_ordenados = palabras_palindromos_ordenadas(conjunto_palabras)

print("Conjunto de palabras:", conjunto_palabras)
print("Palíndromos ordenados por longitud:", palindromos_ordenados)
