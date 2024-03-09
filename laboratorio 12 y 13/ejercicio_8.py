class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_altura_arbol(raiz):
    if raiz is None:
        return 0

    if not raiz.hijos:
        
        return 1

    altura_subarboles = [calcular_altura_arbol(hijo) for hijo in raiz.hijos]
    return 1 + max(altura_subarboles)

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.hijos.extend([nodo2, nodo3])
nodo2.hijos.extend([nodo4, nodo5])

altura_arbol = calcular_altura_arbol(nodo1)

print(f"La altura del árbol es: {altura_arbol}")
