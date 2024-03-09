class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

# Función para imprimir la lista hacia adelante
def imprimir_adelante(nodo):
    while nodo is not None:
        print(nodo.valor, end=" ")
        nodo = nodo.siguiente
    print()

# Función para imprimir la lista hacia atrás
def imprimir_atras(nodo):
    while nodo is not None:
        print(nodo.valor, end=" ")
        nodo = nodo.anterior
    print()

# Función para insertar un nuevo nodo en una posición específica
def insertar_nodo_en_posicion(lista, nuevo_valor, posicion):
    nuevo_nodo = Nodo(nuevo_valor)
    actual = lista

    for _ in range(posicion - 1):
        if actual is not None:
            actual = actual.siguiente
        else:
            break

    if actual is not None:
        nuevo_nodo.siguiente = actual.siguiente
        if actual.siguiente is not None:
            actual.siguiente.anterior = nuevo_nodo
        nuevo_nodo.anterior = actual
        actual.siguiente = nuevo_nodo

# Crear la lista con al menos 5 nodos
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.siguiente = nodo2
nodo2.anterior = nodo1
nodo2.siguiente = nodo3
nodo3.anterior = nodo2
nodo3.siguiente = nodo4
nodo4.anterior = nodo3
nodo4.siguiente = nodo5
nodo5.anterior = nodo4

# Imprimir la lista original hacia adelante
print("Lista Original hacia adelante:")
imprimir_adelante(nodo1)

# Imprimir la lista original hacia atrás
print("Lista Original hacia atrás:")
imprimir_atras(nodo5)

# Insertar un nuevo nodo con el dato 15 en la posición 3
insertar_nodo_en_posicion(nodo1, 15, 3)

# Imprimir la lista con el nuevo nodo hacia adelante
print("\nLista con Nuevo Nodo hacia adelante:")
imprimir_adelante(nodo1)

# Imprimir la lista con el nuevo nodo hacia atrás
print("Lista con Nuevo Nodo hacia atrás:")
imprimir_atras(nodo5)
