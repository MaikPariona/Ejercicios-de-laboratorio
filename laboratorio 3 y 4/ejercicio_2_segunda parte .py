import numpy as np
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
media = np.mean(matriz)
mediana = np.median(matriz)
desviacion_estandar = np.std(matriz)
print("Matriz:")
print(matriz)
print("\nMedia:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)
