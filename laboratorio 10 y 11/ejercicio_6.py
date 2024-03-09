class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

def invertir_cadena_con_pila(cadena):
    pila = Pila()

    
    for caracter in cadena:
        pila.apilar(caracter)

    
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida

cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena_con_pila(cadena_original)

print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
