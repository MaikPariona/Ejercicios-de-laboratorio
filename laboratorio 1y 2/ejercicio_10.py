fibonacci = [0, 1]
while len(fibonacci) < 10:
    num_siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(num_siguiente)

print(f"Los primeros 10 números de la serie Fibonacci son: {fibonacci} ", )
