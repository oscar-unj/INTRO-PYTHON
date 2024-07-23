# restaurante.py

class Plato:
    def __init__(self, nombre, precio, ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


class Menu:
    def __init__(self):
        self.platos = []

    def añadir_plato(self, plato):
        self.platos.append(plato)
        print(f"Plato '{plato.nombre}' añadido al menú.")

    def mostrar_menu(self):
        print("\nMenú del restaurante:")
        for plato in self.platos:
            print(plato)


class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []
        self.total = 0

    def añadir_plato(self, plato):
        self.platos.append(plato)
        self.total += plato.precio
        print(f"Plato '{plato.nombre}' añadido a la orden de {self.cliente.nombre}.")

    def mostrar_orden(self):
        print(f"\nOrden de {self.cliente.nombre}:")
        for plato in self.platos:
            print(plato)
        print(f"Total: ${self.total:.2f}")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ordenes = []

    def realizar_orden(self, orden):
        self.ordenes.append(orden)
        print(f"{self.nombre} ha realizado una nueva orden.")

    def historial_ordenes(self):
        print(f"\nHistorial de ordenes de {self.nombre}:")
        for orden in self.ordenes:
            orden.mostrar_orden()


class Inventario:
    def __init__(self):
        self.ingredientes = {}

    def añadir_ingrediente(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes:
            self.ingredientes[ingrediente] += cantidad
        else:
            self.ingredientes[ingrediente] = cantidad
        print(f"Ingrediente '{ingrediente}' añadido al inventario. Cantidad: {self.ingredientes[ingrediente]}")

    def usar_ingrediente(self, ingrediente, cantidad):
        if ingrediente in self.ingredientes and self.ingredientes[ingrediente] >= cantidad:
            self.ingredientes[ingrediente] -= cantidad
            print(f"Ingrediente '{ingrediente}' utilizado. Cantidad restante: {self.ingredientes[ingrediente]}")
        else:
            print(f"Ingrediente '{ingrediente}' insuficiente en el inventario.")

    def mostrar_inventario(self):
        print("\nInventario del restaurante:")
        for ingrediente, cantidad in self.ingredientes.items():
            print(f"{ingrediente}: {cantidad}")


class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = Menu()
        self.inventario = Inventario()
        self.clientes = []
        self.ventas_totales = 0

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado en el restaurante.")

    def realizar_venta(self, cliente, orden):
        self.ventas_totales += orden.total
        cliente.realizar_orden(orden)
        print(f"Venta realizada para {cliente.nombre}. Total: ${orden.total:.2f}")

    def generar_reporte_ventas(self):
        print(f"\nReporte de ventas del restaurante '{self.nombre}':")
        print(f"Ventas totales: ${self.ventas_totales:.2f}")
        print("Clientes:")
        for cliente in self.clientes:
            print(cliente.nombre)


# Crear instancia del restaurante
restaurante = Restaurante("Buen Sabor")

# Crear y añadir platos al menú
plato1 = Plato("Ensalada César", 10.50, ["lechuga", "crutones", "queso parmesano", "salsa César"])
plato2 = Plato("Pizza Margarita", 12.75, ["masa", "salsa de tomate", "queso mozzarella", "albahaca"])
plato3 = Plato("Spaghetti Bolognese", 15.00, ["spaghetti", "salsa bolognese", "queso parmesano"])

restaurante.menu.añadir_plato(plato1)
restaurante.menu.añadir_plato(plato2)
restaurante.menu.añadir_plato(plato3)

# Mostrar menú del restaurante
restaurante.menu.mostrar_menu()

# Gestionar inventario
restaurante.inventario.añadir_ingrediente("lechuga", 20)
restaurante.inventario.añadir_ingrediente("crutones", 15)
restaurante.inventario.añadir_ingrediente("queso parmesano", 30)
restaurante.inventario.añadir_ingrediente("salsa César", 10)
restaurante.inventario.mostrar_inventario()

# Registrar clientes
cliente1 = Cliente("Alice")
cliente2 = Cliente("Bob")

restaurante.registrar_cliente(cliente1)
restaurante.registrar_cliente(cliente2)

# Crear y realizar órdenes
orden1 = Orden(cliente1)
orden1.añadir_plato(plato1)
orden1.añadir_plato(plato2)

orden2 = Orden(cliente2)
orden2.añadir_plato(plato3)

restaurante.realizar_venta(cliente1, orden1)
restaurante.realizar_venta(cliente2, orden2)

# Mostrar historial de órdenes de un cliente
cliente1.historial_ordenes()

# Generar reporte de ventas
restaurante.generar_reporte_ventas()


# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30

