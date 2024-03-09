def imprimir_tabla_multiplicar(n, multiplicador=1):
    if multiplicador > 10:
        return
    else:
        resultado = n * multiplicador
        print(f"{n} x {multiplicador} = {resultado}")

        imprimir_tabla_multiplicar(n, multiplicador + 1)
imprimir_tabla_multiplicar(6)
