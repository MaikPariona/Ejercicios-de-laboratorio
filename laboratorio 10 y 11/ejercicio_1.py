class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

def imprimir_adelante(nodo):
    while nodo is not None:
        print(nodo.dato, end=" ")
        nodo = nodo.siguiente
    print()

def imprimir_atras(nodo):
    while nodo is not None:
        print(nodo.dato, end=" ")
        nodo = nodo.anterior
    print()

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)

# Enlazar los nodos
nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3

print("Lista Original hacia adelante:")
imprimir_adelante(nodo1)

print("Lista Original hacia atrás:")
imprimir_atras(nodo4)

actual = nodo1
while actual is not None:
    nuevo_nodo = Nodo(actual.dato)
    nuevo_nodo.siguiente = actual.siguiente
    if actual.siguiente is not None:
        actual.siguiente.anterior = nuevo_nodo
    nuevo_nodo.anterior = actual
    actual.siguiente = nuevo_nodo
    actual = nuevo_nodo.siguiente

# Imprimir la lista duplicada hacia adelante
print("Lista Duplicada hacia adelante:")
imprimir_adelante(nodo1)

# Imprimir la lista duplicada hacia atrás
print("Lista Duplicada hacia atrás:")
imprimir_atras(nodo4)
