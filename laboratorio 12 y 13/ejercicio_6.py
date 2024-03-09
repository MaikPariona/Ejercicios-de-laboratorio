class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(raiz):
    if raiz is None:
        return 0

    if not raiz.hijos:
        # El nodo es una hoja
        return 1

    cantidad_nodos_hoja = 0

    for hijo in raiz.hijos:
        cantidad_nodos_hoja += contar_nodos_hoja(hijo)

    return cantidad_nodos_hoja

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.hijos.extend([nodo2, nodo3])
nodo2.hijos.extend([nodo4, nodo5])

cantidad_nodos_hoja = contar_nodos_hoja(nodo1)

print(f"La cantidad de nodos hoja en el árbol es: {cantidad_nodos_hoja}")
