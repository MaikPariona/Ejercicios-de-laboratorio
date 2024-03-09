class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_nodo_maximo(raiz):
    if raiz is None:
        return None

    if not raiz.hijos:
        
        return raiz

    nodos_maximos_subarboles = [encontrar_nodo_maximo(hijo) for hijo in raiz.hijos]
    return max([raiz] + nodos_maximos_subarboles, key=lambda nodo: nodo.valor)

nodo1 = Nodo(10)
nodo2 = Nodo(5)
nodo3 = Nodo(15)
nodo4 = Nodo(3)
nodo5 = Nodo(7)

nodo1.hijos.extend([nodo2, nodo3])
nodo2.hijos.extend([nodo4, nodo5])

nodo_maximo = encontrar_nodo_maximo(nodo1)

if nodo_maximo is not None:
    print(f"El nodo con el valor máximo es: {nodo_maximo.valor}")
else:
    print("El árbol está vacío.")
