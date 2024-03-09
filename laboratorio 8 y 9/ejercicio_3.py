def validar_calificacion(calificacion):
    assert isinstance(calificacion, (int, float)), "La calificación debe ser un número"
    assert 0 <= calificacion <= 10, "La calificación debe estar en el rango de 0 a 10"

    print("La calificación es válida:", calificacion)

try:
    calificacion_usuario = float(input("Ingresa tu calificación: "))
    validar_calificacion(calificacion_usuario)
except ValueError:
    print("Por favor, ingresa un número válido para la calificación.")
except AssertionError as e:
    print(e)
