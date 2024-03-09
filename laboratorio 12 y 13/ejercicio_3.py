from collections import deque

def encontrar_camino_laberinto(laberinto, inicio, destino):
    
    direcciones = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    filas = len(laberinto)
    columnas = len(laberinto[0])

    cola = deque([(inicio[0], inicio[1], 0)])  # (fila, columna, distancia)

    laberinto[inicio[0]][inicio[1]] = -1

    while cola:
        fila, columna, distancia = cola.popleft()

        if (fila, columna) == destino:
            return distancia

        for direccion in direcciones:
            nueva_fila, nueva_columna = fila + direccion[0], columna + direccion[1]

            
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] == 0:
                # Marcar como visitado y agregar a la cola
                laberinto[nueva_fila][nueva_columna] = -1
                cola.append((nueva_fila, nueva_columna, distancia + 1))


    return -1

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

inicio = (0, 0)
destino = (4, 4)

distancia = encontrar_camino_laberinto(laberinto, inicio, destino)

if distancia != -1:
    print(f"El camino más corto desde {inicio} hasta {destino} es de {distancia} pasos.")
else:
    print("No se encontró un camino válido.")
