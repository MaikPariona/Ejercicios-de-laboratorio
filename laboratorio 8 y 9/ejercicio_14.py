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

def eliminar_duplicados(lista):
    if lista.cabeza is None:
        return

    nodos_vistos = set()
    actual = lista.cabeza
    anterior = None

    while actual:
        if actual.dato in nodos_vistos:
            
            anterior.siguiente = actual.siguiente
            actual = None
        else:
           
            nodos_vistos.add(actual.dato)
            anterior = actual
        actual = anterior.siguiente

mi_lista = ListaEnlazada()
mi_lista.agregar_nodo(3)
mi_lista.agregar_nodo(7)
mi_lista.agregar_nodo(3)
mi_lista.agregar_nodo(1)
mi_lista.agregar_nodo(7)

print("Lista original:")
mi_lista.mostrar_lista()

eliminar_duplicados(mi_lista)

print("\nLista sin nodos duplicados:")
mi_lista.mostrar_lista()
