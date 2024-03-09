def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def numeros_primos_en_conjunto(conjunto):
        nuevo_conjunto = set()
        for numero in conjunto:
            if es_primo(numero):
                nuevo_conjunto.add(numero)
        return nuevo_conjunto

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, -2}
conjunto_primos = numeros_primos_en_conjunto(conjunto)

print("Conjunto original:", conjunto)
print("Conjunto de números primos:", conjunto_primos)
