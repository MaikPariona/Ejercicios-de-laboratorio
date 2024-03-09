def mi_funcion(x, y):
    resultado = x + y
    assert resultado == 10, "La función no retornó el valor esperado."
    return resultado

valor_esperado = mi_funcion(4, 6)
print(f"La función retornó el valor esperado: {valor_esperado}")
