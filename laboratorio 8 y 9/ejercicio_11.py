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

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza

        while actual is not None:
            suma += actual.dato
            actual = actual.siguiente

        return suma

mi_lista = ListaEnlazada()
mi_lista.agregar_nodo(3)
mi_lista.agregar_nodo(7)
mi_lista.agregar_nodo(1)

resultado_suma = mi_lista.sumar_nodos()
print(f"La suma de los nodos es: {resultado_suma}")
