def longitud(conjunto, longitud):
    nuevo_conjunto = set()
    for palabra in conjunto:
         if len(palabra) == longitud:
              nuevo_conjunto.add(palabra)
    return nuevo_conjunto

conjunto = {"manzana", "plátano", "naranja", "kiwi", "uva"}
longitud_determinado = 7
conjunto_palabras = longitud(conjunto, longitud_determinado)

print("Conjunto de palabras:", conjunto)
print(f"Palabras con longitud {longitud_determinado}:", conjunto_palabras)
