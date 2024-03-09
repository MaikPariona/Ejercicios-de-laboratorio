class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

def concatenar_listas(lista1, lista2):
    if lista1.cabeza is None:
        lista1.cabeza = lista2.cabeza
    else:
        actual = lista1.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = lista2.cabeza

lista_a = ListaEnlazada()
lista_a.agregar_nodo(3)
lista_a.agregar_nodo(7)
lista_a.agregar_nodo(1)

lista_b = ListaEnlazada()
lista_b.agregar_nodo(4)
lista_b.agregar_nodo(2)
lista_b.agregar_nodo(9)

print("Lista A:")
lista_a.mostrar_lista()

print("\nLista B:")
lista_b.mostrar_lista()

concatenar_listas(lista_a, lista_b)

print("\nLista Concatenada:")
lista_a.mostrar_lista()
