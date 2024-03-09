import numpy as np

def encontrar_maximo(matriz):
    maximo = np.max(matriz)
    return maximo

matriz = np.array([[1, 2, 3],
                           [4, 9, 6],
                           [7, 8, 5]])

elemento_maximo = encontrar_maximo(matriz)

print("Matriz:")
print(matriz)
print("\nElemento máximo:", elemento_maximo)
