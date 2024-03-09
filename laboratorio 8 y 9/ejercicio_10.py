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

    def buscar_nodo(self, valor):
        actual = self.cabeza

        while actual is not None:
            if actual.dato == valor:
                return actual
            actual = actual.siguiente

        return None

mi_lista = ListaEnlazada()
mi_lista.agregar_nodo(3)
mi_lista.agregar_nodo(7)
mi_lista.agregar_nodo(1)

valor_buscado = 7
nodo_encontrado = mi_lista.buscar_nodo(valor_buscado)

if nodo_encontrado:
    print(f"Nodo con el valor {valor_buscado} encontrado.")
else:
    print(f"Nodo con el valor {valor_buscado} no encontrado.")
