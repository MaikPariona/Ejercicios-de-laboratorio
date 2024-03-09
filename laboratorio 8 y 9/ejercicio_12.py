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

    def longitud_lista(self):
        longitud = 0
        actual = self.cabeza

        while actual is not None:
            longitud += 1
            actual = actual.siguiente

        return longitud

mi_lista = ListaEnlazada()
mi_lista.agregar_nodo(3)
mi_lista.agregar_nodo(7)
mi_lista.agregar_nodo(1)

longitud = mi_lista.longitud_lista()
print(f"La longitud de la lista es: {longitud}")
