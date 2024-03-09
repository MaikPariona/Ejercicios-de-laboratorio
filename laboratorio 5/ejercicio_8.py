def es_palindromo(palabra):
    palabra = ''.join(palabra.lower().split())
    return palabra == palabra[::-1]

def palabras_palindromos(conjunto_palabras):
    nuevo_conjunto = set()
    for palabra in conjunto_palabras:
        if es_palindromo(palabra):
            nuevo_conjunto.add(palabra)
    return nuevo_conjunto

conjunto_palabras = {"Level", "Ana lava lana", "casa", "radar", "civic"}
conjunto_palindromos = palabras_palindromos(conjunto_palabras)

print("Conjunto de palabras:", conjunto_palabras)
print("Palabras que son palíndromos:", conjunto_palindromos)
