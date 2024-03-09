def son_anagramas(palabra1, palabra2):
    return set(palabra1.lower()) == set(palabra2.lower())

def palabras_anagramas(conjunto_palabras):
    anagramas = set()
    for palabra1 in conjunto_palabras:
        for palabra2 in conjunto_palabras:
            if palabra1 != palabra2 and son_anagramas(palabra1, palabra2):
                anagramas.add(palabra1)
                anagramas.add(palabra2)
    return anagramas

conjunto_palabras = {"Cara", "arca", "raca", "Lácteo", "Nido"}
conjunto_anagramas = palabras_anagramas(conjunto_palabras)

print("Conjunto de palabras:", conjunto_palabras)
print("Palabras que son anagramas:", conjunto_anagramas)
