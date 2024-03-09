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

def invertir_lista(lista):
    anterior = None
    actual = lista.cabeza

    while actual:
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente

    lista.cabeza = anterior

mi_lista = ListaEnlazada()
mi_lista.agregar_nodo(3)
mi_lista.agregar_nodo(7)
mi_lista.agregar_nodo(1)

print("Lista original:")
mi_lista.mostrar_lista()

invertir_lista(mi_lista)

print("\nLista invertida:")
mi_lista.mostrar_lista()
