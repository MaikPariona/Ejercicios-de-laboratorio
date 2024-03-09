cadena = str((input("Ingrese una cadena de texto: ")))
cadena_invertida = ""
for caracter in reversed(cadena):
    cadena_invertida += caracter
print(f"Inversión de la cadena: {cadena_invertida}")

