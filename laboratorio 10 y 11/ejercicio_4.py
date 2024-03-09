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


def eliminar_nodos_duplicados(lista):
    valores_set = set()
    actual = lista

    while actual is not None:
        if actual.valor not in valores_set:
            valores_set.add(actual.valor)
            actual = actual.siguiente
        else:
            siguiente_nodo = actual.siguiente
            if siguiente_nodo is not None:
                siguiente_nodo.anterior = actual.anterior
            actual.anterior.siguiente = siguiente_nodo
            actual = siguiente_nodo


nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(2)
nodo5 = Nodo(4)
nodo6 = Nodo(1)

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


eliminar_nodos_duplicados(nodo1)


print("\nLista sin Nodos Duplicados hacia adelante:")
imprimir_atras(nodo6)
