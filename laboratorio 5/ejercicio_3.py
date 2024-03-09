def numeros_divisibles(conjunto, divisor):
    nuevo_conjunto = set()
    for numero in conjunto:
         if numero % divisor == 0:
              nuevo_conjunto.add(numero)
    return nuevo_conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3
conjunto_resultado = numeros_divisibles(conjunto, divisor)
print("Conjunto original:", conjunto)
print(f"Números divisibles por {divisor}:", conjunto_resultado)
