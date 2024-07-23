# restaurante_tk.py

import tkinter as tk
from tkinter import messagebox

class Platillo:
    def __init__(self, nombre, precio, ingredientes):
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - Ingredientes: {', '.join(self.ingredientes)}"

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.orden = []

    def agregar_orden(self, platillo):
        self.orden.append(platillo)
        return f"Platillo '{platillo.nombre}' agregado a la orden de la mesa {self.numero}."

    def eliminar_orden(self, platillo_nombre):
        for platillo in self.orden:
            if platillo.nombre == platillo_nombre:
                self.orden.remove(platillo)
                return f"Platillo '{platillo.nombre}' eliminado de la orden de la mesa {self.numero}."
        return f"Platillo '{platillo_nombre}' no encontrado en la orden de la mesa {self.numero}."

    def obtener_cuenta(self):
        total = sum(platillo.precio for platillo in self.orden)
        return f"Cuenta total para la mesa {self.numero}: ${total:.2f}"

    def __str__(self):
        return f"Mesa {self.numero} - Orden: {', '.join(platillo.nombre for platillo in self.orden) or 'Vacía'}"

class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.platillos = []
        self.mesas = {}

    def agregar_platillo(self, platillo):
        self.platillos.append(platillo)
        return f"Platillo '{platillo.nombre}' agregado al menú."

    def agregar_mesa(self, mesa):
        self.mesas[mesa.numero] = mesa
        return f"Mesa {mesa.numero} agregada al restaurante."

    def mostrar_menu(self):
        return "\n".join(str(platillo) for platillo in self.platillos)

    def mostrar_mesas(self):
        return "\n".join(str(mesa) for mesa in self.mesas.values())

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Restaurante")

        self.restaurante = Restaurante("El Buen Sabor")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Gestión de Restaurante", font=("Arial", 16))
        self.label.pack(pady=10)

        self.menu_label = tk.Label(self.frame, text="Menú")
        self.menu_label.pack()

        self.menu_text = tk.Text(self.frame, height=10, width=50)
        self.menu_text.pack()

        self.mesas_label = tk.Label(self.frame, text="Mesas")
        self.mesas_label.pack()

        self.mesas_text = tk.Text(self.frame, height=10, width=50)
        self.mesas_text.pack()

        self.actualizar_button = tk.Button(self.frame, text="Actualizar", command=self.actualizar)
        self.actualizar_button.pack(pady=10)

        self.platillo_label = tk.Label(self.frame, text="Añadir Platillo (Nombre, Precio, Ingredientes):")
        self.platillo_label.pack()
        self.platillo_entry = tk.Entry(self.frame)
        self.platillo_entry.pack()

        self.añadir_platillo_button = tk.Button(self.frame, text="Añadir Platillo", command=self.añadir_platillo)
        self.añadir_platillo_button.pack(pady=5)

        self.mesa_label = tk.Label(self.frame, text="Agregar Mesa (Número):")
        self.mesa_label.pack()
        self.mesa_entry = tk.Entry(self.frame)
        self.mesa_entry.pack()

        self.añadir_mesa_button = tk.Button(self.frame, text="Agregar Mesa", command=self.añadir_mesa)
        self.añadir_mesa_button.pack(pady=5)

        self.numero_mesa_label = tk.Label(self.frame, text="Número de Mesa:")
        self.numero_mesa_label.pack()
        self.numero_mesa_entry = tk.Entry(self.frame)
        self.numero_mesa_entry.pack()

        self.platillo_orden_label = tk.Label(self.frame, text="Nombre del Platillo:")
        self.platillo_orden_label.pack()
        self.platillo_orden_entry = tk.Entry(self.frame)
        self.platillo_orden_entry.pack()

        self.agregar_orden_button = tk.Button(self.frame, text="Agregar a Orden", command=self.agregar_orden)
        self.agregar_orden_button.pack(pady=5)

        self.eliminar_orden_button = tk.Button(self.frame, text="Eliminar de Orden", command=self.eliminar_orden)
        self.eliminar_orden_button.pack(pady=5)

        self.obtener_cuenta_button = tk.Button(self.frame, text="Obtener Cuenta", command=self.obtener_cuenta)
        self.obtener_cuenta_button.pack(pady=5)

        self.salir_button = tk.Button(self.frame, text="Salir", command=root.quit)
        self.salir_button.pack(pady=10)

    def actualizar(self):
        self.menu_text.delete(1.0, tk.END)
        self.menu_text.insert(tk.END, self.restaurante.mostrar_menu())

        self.mesas_text.delete(1.0, tk.END)
        self.mesas_text.insert(tk.END, self.restaurante.mostrar_mesas())

    def añadir_platillo(self):
        datos = self.platillo_entry.get().split(", ")
        if len(datos) >= 3:
            nombre = datos[0]
            try:
                precio = float(datos[1])
            except ValueError:
                messagebox.showwarning("Advertencia", "El precio debe ser un número.")
                return
            ingredientes = datos[2:]
            platillo = Platillo(nombre, precio, ingredientes)
            mensaje = self.restaurante.agregar_platillo(platillo)
            messagebox.showinfo("Añadir Platillo", mensaje)
            self.platillo_entry.delete(0, tk.END)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduzca los datos del platillo en el formato correcto.")

    def añadir_mesa(self):
        numero = self.mesa_entry.get()
        if numero.isdigit():
            mesa = Mesa(int(numero))
            mensaje = self.restaurante.agregar_mesa(mesa)
            messagebox.showinfo("Agregar Mesa", mensaje)
            self.mesa_entry.delete(0, tk.END)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "El número de mesa debe ser un número.")

    def agregar_orden(self):
        numero_mesa = self.numero_mesa_entry.get()
        platillo_nombre = self.platillo_orden_entry.get()

        if numero_mesa.isdigit():
            numero_mesa = int(numero_mesa)
            mesa = self.restaurante.mesas.get(numero_mesa)
            platillo = next((p for p in self.restaurante.platillos if p.nombre == platillo_nombre), None)

            if mesa and platillo:
                mensaje = mesa.agregar_orden(platillo)
                messagebox.showinfo("Agregar a Orden", mensaje)
                self.actualizar()
            else:
                messagebox.showwarning("Advertencia", "Mesa o platillo no encontrado.")
        else:
            messagebox.showwarning("Advertencia", "El número de mesa debe ser un número.")

    def eliminar_orden(self):
        numero_mesa = self.numero_mesa_entry.get()
        platillo_nombre = self.platillo_orden_entry.get()

        if numero_mesa.isdigit():
            numero_mesa = int(numero_mesa)
            mesa = self.restaurante.mesas.get(numero_mesa)

            if mesa:
                mensaje = mesa.eliminar_orden(platillo_nombre)
                messagebox.showinfo("Eliminar de Orden", mensaje)
                self.actualizar()
            else:
                messagebox.showwarning("Advertencia", "Mesa no encontrada.")
        else:
            messagebox.showwarning("Advertencia", "El número de mesa debe ser un número.")

    def obtener_cuenta(self):
        numero_mesa = self.numero_mesa_entry.get()

        if numero_mesa.isdigit():
            numero_mesa = int(numero_mesa)
            mesa = self.restaurante.mesas.get(numero_mesa)

            if mesa:
                mensaje = mesa.obtener_cuenta()
                messagebox.showinfo("Obtener Cuenta", mensaje)
            else:
                messagebox.showwarning("Advertencia", "Mesa no encontrada.")
        else:
            messagebox.showwarning("Advertencia", "El número de mesa debe ser un número.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30

