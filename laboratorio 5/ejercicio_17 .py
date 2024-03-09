def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    return sorted(palabras_filtradas)


conjunto_palabras = {"manzana", "kiwi", "banana", "uva", "naranja"}
longitud_determinada = 4
palabras_filtradas_ordenadas = palabras_con_longitud_ordenadas(conjunto_palabras, longitud_determinada)

print("Conjunto de palabras:", conjunto_palabras)
print(f"Palabras con longitud {longitud_determinada} ordenadas:", palabras_filtradas_ordenadas)
