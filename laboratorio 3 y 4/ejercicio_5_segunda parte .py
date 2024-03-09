import numpy as np

def matriz_covarianza(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener el mismo número de columnas")

    matriz_concatenada = np.concatenate((matriz1, matriz2), axis=1)

    covarianza = np.cov(matriz_concatenada, rowvar=False)

    return covarianza

matriz1_ejemplo = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

matriz2_ejemplo = np.array([[9, 8, 7],
                            [6, 5, 4],
                            [3, 2, 1]])

matriz_covarianza_resultado = matriz_covarianza(matriz1_ejemplo, matriz2_ejemplo)

print("Matriz de covarianza:")
print(matriz_covarianza_resultado)
