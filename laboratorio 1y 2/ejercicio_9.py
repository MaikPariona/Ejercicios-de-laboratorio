cadena = input("Ingrese una cadena de texto: ")
cadena = cadena.lower()
conteo_vocales = 0
for caracter in cadena:
    if caracter in "aeiouáéíóú":
        conteo_vocales += 1
print(f"El número de vocales en la cadena es: {conteo_vocales}")
