def verificar_anidacion(expresion):
    pila = []

    pares_operadores = {'(': ')', '[': ']', '{': '}'}

    for char in expresion:
        if char in pares_operadores.keys():
            pila.append(char)
        elif char in pares_operadores.values():
            
            if not pila or pares_operadores[pila.pop()] != char:
               
                return False


    return not pila


expresion_correcta = "{(3+4)*(5-2)}"
expresion_incorrecta = "{(3+4)*(5-2)"

if verificar_anidacion(expresion_correcta):
    print(f"La expresión '{expresion_correcta}' está correctamente anidada.")
else:
    print(f"La expresión '{expresion_correcta}' no está correctamente anidada.")

if verificar_anidacion(expresion_incorrecta):
    print(f"La expresión '{expresion_incorrecta}' está correctamente anidada.")
else:
    print(f"La expresión '{expresion_incorrecta}' no está correctamente anidada.")
