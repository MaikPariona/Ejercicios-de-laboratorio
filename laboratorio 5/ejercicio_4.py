def numeros_en_ambos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
conjunto_resultado = numeros_en_ambos(conjunto1, conjunto2)

print("Primer conjunto:", conjunto1)
print("Segundo conjunto:", conjunto2)
print("Números en ambos conjuntos:", conjunto_resultado)
