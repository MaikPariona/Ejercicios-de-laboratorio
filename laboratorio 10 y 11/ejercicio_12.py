def calcular_expresion(expresion):
    pila_numeros = []
    pila_operadores = {'+': lambda x, y: x + y,
                       '-': lambda x, y: x - y,
                       '*': lambda x, y: x * y,
                       '/': lambda x, y: x / y}

    def aplicar_operador():
        operador = pila_operadores[pila_operadores.pop()]
        segundo_numero = pila_numeros.pop()
        primer_numero = pila_numeros.pop()
        resultado = operador(primer_numero, segundo_numero)
        pila_numeros.append(resultado)

    for caracter in expresion:
        if caracter.isdigit():
            pila_numeros.append(int(caracter))
        elif caracter in pila_operadores:
            pila_operadores.append(caracter)
        elif caracter == ' ':
            continue  
        else:
            raise ValueError(f"Caracter no reconocido: {caracter}")

    while pila_operadores:
        aplicar_operador()

    if len(pila_numeros) == 1:
        return pila_numeros[0]
    else:
        raise ValueError("Expresión no válida")

expresion = "3 + 4 * 2 / ( 1 - 5 )"
try:
    resultado = calcular_expresion(expresion)
    print(f"Resultado de la expresión '{expresion}': {resultado}")
except ValueError as e:
    print(f"Error: {e}")
