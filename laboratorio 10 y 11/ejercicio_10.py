def ordenar_pila_ascendente(pila):
    pila_auxiliar = []

    while pila:
        
        temp = pila.pop()

        
        while pila_auxiliar and pila_auxiliar[-1] > temp:
            pila.append(pila_auxiliar.pop())

        
        pila_auxiliar.append(temp)

    
    while pila_auxiliar:
        pila.append(pila_auxiliar.pop())

pila_original = [5, 3, 8, 1, 2]
print("Pila original:", pila_original)

ordenar_pila_ascendente(pila_original)

print("Pila ordenada ascendente:", pila_original)
