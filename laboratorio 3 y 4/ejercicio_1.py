def numeros_pares(n):
    if n<= 100:
        if n % 2 == 0:
            print(n)
        numeros_pares(n+1)
numeros_pares(1)