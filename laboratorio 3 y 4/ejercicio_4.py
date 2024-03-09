def imprimir_piramide_invertida(n, fila=1):
    if fila> n:
        return
    else:
        print(" " * (n-fila), end="")
        
        for i in range(n,n-fila,-1):
            print(i, end=" ")
        print()
        
        imprimir_piramide_invertida(n,fila+1)
imprimir_piramide_invertida(8)
