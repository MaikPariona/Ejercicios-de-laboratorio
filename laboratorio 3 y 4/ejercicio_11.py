import numpy as np
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

numero = 2

resultado = np.multiply(numero, matriz)

print("Matriz original:")
print(matriz)

print("\nResultado multiplicando por",numero," :")
print(resultado)
