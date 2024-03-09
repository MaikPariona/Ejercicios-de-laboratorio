cantidad = int(input("ingrese la cantidad de numeros que desea ordenar: "))
lista = []
for i in range(1,cantidad+1):
    num = float(input(f"ingrese el numero {i} : "))
    lista.append(num)
lista.sort()
print(f"la lista ordenada es:{lista} ")

