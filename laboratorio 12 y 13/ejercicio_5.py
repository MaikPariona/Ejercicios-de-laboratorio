class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_arbol(raiz):
    if raiz is None:
        return 0

    cantidad_nodos = 1  # Contar el nodo actual

    for hijo in raiz.hijos:
        cantidad_nodos += contar_nodos_arbol(hijo)

    return cantidad_nodos

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.hijos.extend([nodo2, nodo3])
nodo2.hijos.extend([nodo4, nodo5])

cantidad_nodos = contar_nodos_arbol(nodo1)

print(f"La cantidad de nodos en el árbol es: {cantidad_nodos}")
