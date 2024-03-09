def submatriz_mayor_suma(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    sumas_acumulativas = [[0] * (columnas + 1) for _ in range(filas + 1)]
    for i in range(1, filas + 1):
        for j in range(1, columnas + 1):
            sumas_acumulativas[i][j] = matriz[i - 1][j - 1] + sumas_acumulativas[i - 1][j] + sumas_acumulativas[i][j - 1] - sumas_acumulativas[i - 1][j - 1]

    max_suma = float('-inf')
    coordenadas = None
    for i_inicio in range(filas):
        for i_fin in range(i_inicio + 1, filas + 1):
            for j_inicio in range(columnas):
                for j_fin in range(j_inicio + 1, columnas + 1):
                    suma_actual = sumas_acumulativas[i_fin][j_fin] - sumas_acumulativas[i_inicio][j_fin] - sumas_acumulativas[i_fin][j_inicio] + sumas_acumulativas[i_inicio][j_inicio]
                    if suma_actual > max_suma:
                        max_suma = suma_actual
                        coordenadas = ((i_inicio, j_inicio), (i_fin - 1, j_fin - 1))

    submatriz = [fila[coordenadas[0][1]:coordenadas[1][1] + 1] for fila in matriz[coordenadas[0][0]:coordenadas[1][0] + 1]]

    return submatriz
