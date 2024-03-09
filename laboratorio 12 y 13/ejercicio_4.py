class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"Tarea agregada al proyecto '{self.nombre}': {tarea}")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            print(f"Tarea completada en el proyecto '{self.nombre}': {self.tareas[indice]}")
        else:
            print("Índice de tarea no válido.")

    def mostrar_proxima_tarea_pendiente(self):
        tareas_pendientes = [tarea for tarea in self.tareas if not tarea.completada]

        if tareas_pendientes:
            print(f"Próxima tarea pendiente en el proyecto '{self.nombre}':")
            print(tareas_pendientes[0])
        else:
            print(f"No hay tareas pendientes en el proyecto '{self.nombre}'.")

class SistemaGestionTareas:
    def __init__(self):
        self.proyectos = []

    def agregar_proyecto(self, nombre):
        proyecto = Proyecto(nombre)
        self.proyectos.append(proyecto)
        print(f"Proyecto agregado: {nombre}")

    def agregar_tarea_a_proyecto(self, proyecto_indice, descripcion):
        if 0 <= proyecto_indice < len(self.proyectos):
            self.proyectos[proyecto_indice].agregar_tarea(descripcion)
        else:
            print("Índice de proyecto no válido.")

    def marcar_completada_en_proyecto(self, proyecto_indice, tarea_indice):
        if 0 <= proyecto_indice < len(self.proyectos):
            self.proyectos[proyecto_indice].marcar_completada(tarea_indice)
        else:
            print("Índice de proyecto no válido.")

    def mostrar_proxima_tarea_pendiente_en_proyecto(self, proyecto_indice):
        if 0 <= proyecto_indice < len(self.proyectos):
            self.proyectos[proyecto_indice].mostrar_proxima_tarea_pendiente()
        else:
            print("Índice de proyecto no válido.")

sistema_tareas = SistemaGestionTareas()

sistema_tareas.agregar_proyecto("Proyecto Personal")
sistema_tareas.agregar_tarea_a_proyecto(0, "Hacer ejercicio")
sistema_tareas.agregar_tarea_a_proyecto(0, "Leer un libro")

sistema_tareas.agregar_proyecto("Proyecto Laboral")
sistema_tareas.agregar_tarea_a_proyecto(1, "Preparar presentación")
sistema_tareas.agregar_tarea_a_proyecto(1, "Enviar informe")

sistema_tareas.mostrar_proxima_tarea_pendiente_en_proyecto(0)

sistema_tareas.marcar_completada_en_proyecto(0, 0)

sistema_tareas.mostrar_proxima_tarea_pendiente_en_proyecto(0)
