from collections import deque

def es_palindroma(palabra):
    
    palabra_procesada = ''.join(palabra.lower().split())
    
   
    cola = deque()

    
    for caracter in palabra_procesada:
        cola.append(caracter)

    
    while len(cola) > 1:
        if cola.popleft() != cola.pop():
            return False

    return True

palabra1 = "reconocer"
palabra2 = "Python"

print(f"¿'{palabra1}' es palíndroma? {es_palindroma(palabra1)}")
print(f"¿'{palabra2}' es palíndroma? {es_palindroma(palabra2)}")
