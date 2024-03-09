def imprimir_piramide(n, fila=1):
    if fila > n:
        return
    else:
        print(" " * (n - fila), end="")
        
        for i in range(1, fila + 1):
            print(i, end=" ")
        print()
        
        imprimir_piramide(n, fila + 1)

imprimir_piramide(8)
