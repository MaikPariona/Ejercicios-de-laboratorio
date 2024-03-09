def es_palindromo(frase):
    pila = []
    frase_procesada = ''.join(c.lower() for c in frase if c.isalnum())

    for caracter in frase_procesada:
        pila.append(caracter)

    for caracter in frase_procesada:
        if caracter != pila.pop():
            return False

    return True

palabra_palindromo = "reconocer"
frase_palindromo = "Anita lava la tina"

if es_palindromo(palabra_palindromo):
    print(f"'{palabra_palindromo}' es un palíndromo.")
else:
    print(f"'{palabra_palindromo}' no es un palíndromo.")

if es_palindromo(frase_palindromo):
    print(f"'{frase_palindromo}' es un palíndromo.")
else:
    print(f"'{frase_palindromo}' no es un palíndromo.")
