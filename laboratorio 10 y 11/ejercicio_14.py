class SistemaDeshacer:
    def __init__(self):
        self.pila_acciones = []
        self.pila_deshacer = []

    def realizar_accion(self, accion):
        self.pila_acciones.append(accion)
        

    def deshacer_accion(self):
        if self.pila_acciones:
            accion_deshacer = self.pila_acciones.pop()
            self.pila_deshacer.append(accion_deshacer)
            
            print(f"Deshaciendo: {accion_deshacer}")
        else:
            print("No hay acciones para deshacer.")

    def rehacer_accion(self):
        if self.pila_deshacer:
            accion_rehacer = self.pila_deshacer.pop()
            self.pila_acciones.append(accion_rehacer)
            
            print(f"Rehaciendo: {accion_rehacer}")
        else:
            print("No hay acciones para rehacer.")

sistema_deshacer = SistemaDeshacer()

sistema_deshacer.realizar_accion("Escribir texto")
sistema_deshacer.realizar_accion("Eliminar texto")
sistema_deshacer.realizar_accion("Modificar formato")

sistema_deshacer.deshacer_accion()
sistema_deshacer.deshacer_accion()

sistema_deshacer.rehacer_accion()
