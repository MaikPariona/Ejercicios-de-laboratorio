class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

def imprimir_adelante(nodo):
    while nodo is not None:
        print(nodo.valor, end=" ")
        nodo = nodo.siguiente
    print()

def imprimir_atras(nodo):
    while nodo is not None:
        print(nodo.valor, end=" ")
        nodo = nodo.anterior
    print()

def contar_pares_impares(lista):
    contador_pares = 0
    contador_impares = 0
    actual = lista

    while actual is not None:
        if actual.valor % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1
        actual = actual.siguiente

    return contador_pares, contador_impares

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)
nodo8 = Nodo(8)
nodo9 = Nodo(9)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4
nodo5.siguiente = nodo6
nodo6.anterior = nodo5
nodo6.siguiente = nodo7
nodo7.anterior = nodo6
nodo7.siguiente = nodo8
nodo8.anterior = nodo7
nodo8.siguiente = nodo9
nodo9.anterior = nodo8

print("Lista Original hacia adelante:")
imprimir_adelante(nodo1)

print("Lista Original hacia atrás:")
imprimir_atras(nodo9)

pares, impares = contar_pares_impares(nodo1)
print(f"\nNúmero de nodos con datos pares: {pares}")
print(f"Número de nodos con datos impares: {impares}")
