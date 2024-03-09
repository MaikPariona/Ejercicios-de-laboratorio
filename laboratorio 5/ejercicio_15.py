def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def numeros_primos_ordenados_menor_a_mayor(conjunto_numeros):
    primos = {numero for numero in conjunto_numeros if es_primo(numero)}
    ordenado = sorted(primos)
    nuevo_conjunto= set(ordenado)
    return nuevo_conjunto

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_primos_ordenados = numeros_primos_ordenados_menor_a_mayor(conjunto)

print("Conjunto de números:", conjunto)
print("Números primos ordenados de menor a mayor:", conjunto_primos_ordenados)
