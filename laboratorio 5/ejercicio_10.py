def palabras_con_letra(conjunto, letra):
    nuevo_conjunto = set()
    for palabra in conjunto:
         if letra in palabra:
              nuevo_conjunto.add(palabra)
    return nuevo_conjunto

conjunto = {"manzana", "plátano", "naranja", "kiwi", "uva"}
letra_determinada = "n"
conjunto_palabras_con_letra = palabras_con_letra(conjunto, letra_determinada)

print("Conjunto de palabras:", conjunto)
print(f"Palabras que contienen la letra '{letra_determinada}':", conjunto_palabras_con_letra)
