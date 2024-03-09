def evaluar_expresion_posfija(expresion):
    pila = []

    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def multiplicacion(a, b):
        return a * b

    def division(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Error: División por cero")

    operadores = {'+': suma, '-': resta, '*': multiplicacion, '/': division}

    tokens = expresion.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            
            pila.append(float(token))
        elif token in operadores:
            
            if len(pila) < 2:
                raise ValueError("Error: Expresión no válida")
            operand2 = pila.pop()
            operand1 = pila.pop()
            resultado = operadores[token](operand1, operand2)
            pila.append(resultado)
        else:
            raise ValueError("Error: Token no reconocido")

    if len(pila) == 1:
        return pila[0]
    else:
        raise ValueError("Error: Expresión no válida")

expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print(f"Resultado de la expresión '{expresion_posfija}': {resultado}")
