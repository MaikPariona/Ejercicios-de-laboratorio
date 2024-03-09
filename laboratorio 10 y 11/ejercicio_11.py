def eliminar_duplicados_pila(pila):
    conjunto_vistos = set()
    pila_temporal = []

    while pila:
        elemento = pila.pop()

        if elemento not in conjunto_vistos:
            
            conjunto_vistos.add(elemento)
            pila_temporal.append(elemento)

    
    while pila_temporal:
        pila.append(pila_temporal.pop())

pila_original = [3, 5, 2, 3, 8, 5, 1, 2]

print("Pila original:", pila_original)

eliminar_duplicados_pila(pila_original)

print("Pila sin elementos duplicados:", pila_original)
