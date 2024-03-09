def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_filtradas = {palabra for palabra in conjunto_palabras if letra in palabra.lower()}
    return sorted(palabras_filtradas, key=len, reverse=True)


conjunto_palabras = {"manzana", "kiwi", "banana", "uva", "naranja"}
letra_determinada = "a"
palabras_filtradas_ordenadas = palabras_con_letra_ordenadas(conjunto_palabras, letra_determinada)

print("Conjunto de palabras:", conjunto_palabras)
print(f"Palabras que contienen la letra '{letra_determinada}' ordenadas de mayor a menor:", palabras_filtradas_ordenadas)
