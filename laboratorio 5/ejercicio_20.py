def palabras_palindromos_con_longitud_ordenadas(conjunto_palabras, longitud):
    palindromos_filtrados = {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra.lower() == palabra.lower()[::-1]}
    return sorted(palindromos_filtrados)


conjunto_palabras = {"radar", "level", "civic", "python", "Able was I ere I saw Elba"}
longitud_determinada = 5
palindromos_con_longitud_ordenados = palabras_palindromos_con_longitud_ordenadas(conjunto_palabras, longitud_determinada)

print("Conjunto original de palabras:", conjunto_palabras)
print(f"Palíndromos con longitud {longitud_determinada} ordenados:", palindromos_con_longitud_ordenados)
