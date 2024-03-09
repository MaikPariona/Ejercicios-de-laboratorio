def numeros_en_segundo_conjunto_no_en_primero(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
conjunto_resultado = numeros_en_segundo_conjunto_no_en_primero(conjunto1, conjunto2)

print("Primer conjunto:", conjunto1)
print("Segundo conjunto:", conjunto2)
print("Números en el segundo conjunto pero no en el primero:", conjunto_resultado)
