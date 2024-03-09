def palabras_letra(conjunto, letra):
    nuevo_conjunto = set()
    for palabra in conjunto:
        if palabra.startswith(letra):
            nuevo_conjunto.add(palabra)
    return nuevo_conjunto

conjunto = {"brandon", "jesus", "cesar", "javier", "hola", "cecilia","jazmin"}
letra = "j"
conjunto_resultado = palabras_letra(conjunto, letra)

print("Conjunto original:", conjunto)
print(f"Palabras que comienzan con '{letra}':", conjunto_resultado)
