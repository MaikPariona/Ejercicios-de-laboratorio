from collections import deque

class SistemaGestionPedidos:
    def __init__(self):
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):
        self.cola_pedidos.append(pedido)
        print(f"Pedido añadido: {pedido}")

    def procesar_pedido(self):
        if self.cola_pedidos:
            pedido = self.cola_pedidos.popleft()
            print(f"Procesando pedido: {pedido}")
        else:
            print("No hay pedidos para procesar.")

    def mostrar_estado_cola(self):
        if self.cola_pedidos:
            print("Estado actual de la cola de pedidos:")
            for i, pedido in enumerate(self.cola_pedidos, start=1):
                print(f"{i}. {pedido}")
        else:
            print("La cola de pedidos está vacía.")

sistema_pedidos = SistemaGestionPedidos()

sistema_pedidos.agregar_pedido("Pizza")
sistema_pedidos.agregar_pedido("Hamburguesa")
sistema_pedidos.agregar_pedido("Ensalada")

sistema_pedidos.mostrar_estado_cola()

sistema_pedidos.procesar_pedido()
sistema_pedidos.procesar_pedido()

sistema_pedidos.mostrar_estado_cola()
