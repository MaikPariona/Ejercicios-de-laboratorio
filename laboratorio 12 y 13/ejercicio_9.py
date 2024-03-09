class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def calcular_profundidad_nodo(raiz, valor_buscado, profundidad_actual=0):
    if raiz is None:
        return None

    if raiz.valor == valor_buscado:
        return profundidad_actual

    for hijo in raiz.hijos:
        profundidad_nodo = calcular_profundidad_nodo(hijo, valor_buscado, profundidad_actual + 1)
        if profundidad_nodo is not None:
            return profundidad_nodo

    return None

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

nodo1.hijos.extend([nodo2, nodo3])
nodo2.hijos.extend([nodo4, nodo5])


valor_buscado = 4
profundidad_nodo = calcular_profundidad_nodo(nodo1, valor_buscado)

if profundidad_nodo is not None:
    print(f"La profundidad del nodo con valor {valor_buscado} es: {profundidad_nodo}")
else:
    print(f"No se encontró el nodo con valor {valor_buscado}")
