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

def invertir_lista(lista):
    actual = lista
    while actual is not None:
        actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
        actual = actual.anterior

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

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


print("Lista Original hacia adelante:")
imprimir_adelante(nodo1)

print("Lista Original hacia atrás:")
imprimir_atras(nodo6)


invertir_lista(nodo1)


print("\nLista Invertida hacia adelante:")
imprimir_adelante(nodo6)


print("Lista Invertida hacia atrás:")
imprimir_atras(nodo1)
