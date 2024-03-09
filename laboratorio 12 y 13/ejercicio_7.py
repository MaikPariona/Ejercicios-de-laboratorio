class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(raiz):
    if raiz is None:
        return 0

    if not raiz.hijos:

        return 0

    cantidad_nodos_internos = 1  

    for hijo in raiz.hijos:
        cantidad_nodos_internos += contar_nodos_internos(hijo)

    return cantidad_nodos_internos

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.hijos.extend([nodo2, nodo3])
nodo2.hijos.extend([nodo4, nodo5])

cantidad_nodos_internos = contar_nodos_internos(nodo1)

print(f"La cantidad de nodos internos en el árbol es: {cantidad_nodos_internos}")
