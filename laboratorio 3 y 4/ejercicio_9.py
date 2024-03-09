import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

filas, columnas = matriz.shape

fila_central = filas // 2
columna_central = columnas // 2

elemento_central = matriz[fila_central, columna_central]

print("Elemento central de la matriz:", elemento_central)
