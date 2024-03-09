import numpy as np

matriz1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matriz2 = np.array([
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
])

filas1, columnas1 = matriz1.shape
filas2, columnas2 = matriz2.shape
if columnas1 == columnas2:
    if filas1 == filas2:
        resultado = matriz1 + matriz2
        print("Matriz Resultante:")
        print(resultado)
    else:
        filas_max = max(filas1, filas2)
        if filas1 < filas_max:
            matriz1 = np.vstack([matriz1, np.zeros((filas_max - filas1, columnas1), dtype=matriz1.dtype)])
        if filas2 < filas_max:
            matriz2 = np.vstack([matriz2, np.zeros((filas_max - filas2, columnas2), dtype=matriz2.dtype)])

        resultado = matriz1 + matriz2
        print("Matriz Resultante:")
        print(resultado)
else:
    print("Las matrices no son compatibles para la suma.")
