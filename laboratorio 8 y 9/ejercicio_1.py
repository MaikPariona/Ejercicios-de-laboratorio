def validar_edad(edad):
    assert isinstance(edad, int), "La edad debe ser un número entero."
    assert 0 <= edad, "La edad debe ser positivo."

try:
    edad_usuario = int(input("Ingresa tu edad: "))
    validar_edad(edad_usuario)
    print("Edad válida.")
except ValueError:
    print("Error: Ingresa un número entero para la edad.")
except AssertionError as e:
    print(f"Error: {e}")
