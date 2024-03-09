palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
palabra = palabra.replace(" ", "")
palabra = palabra.replace("á", "a")
palabra = palabra.replace("é", "e")
palabra = palabra.replace("í", "i")
palabra = palabra.replace("ó", "o")
palabra = palabra.replace("ú", "u")
a = 0
b = len(palabra) - 1
palindromo = True  
while a < b:
    if palabra[a] != palabra[b]:
        palindromo = False
        break
    a += 1
    b -= 1

if palindromo== True:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")