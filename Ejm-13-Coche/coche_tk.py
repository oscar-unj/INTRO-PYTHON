# coche_tk.py

import tkinter as tk
from tkinter import messagebox

class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.modelo} está ahora encendido."
        else:
            return f"El {self.modelo} ya está encendido."

    def detener(self):
        if self.encendido:
            self.encendido = False
            return f"El {self.modelo} está ahora apagado."
        else:
            return f"El {self.modelo} ya está apagado."

    def obtener_informacion(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Coches")

        self.coches = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Gestión de Coches", font=("Arial", 16))
        self.label.pack(pady=10)

        self.marca_label = tk.Label(self.frame, text="Marca:")
        self.marca_label.pack()
        self.marca_entry = tk.Entry(self.frame)
        self.marca_entry.pack()

        self.modelo_label = tk.Label(self.frame, text="Modelo:")
        self.modelo_label.pack()
        self.modelo_entry = tk.Entry(self.frame)
        self.modelo_entry.pack()

        self.año_label = tk.Label(self.frame, text="Año:")
        self.año_label.pack()
        self.año_entry = tk.Entry(self.frame)
        self.año_entry.pack()

        self.add_button = tk.Button(self.frame, text="Añadir Coche", command=self.añadir_coche)
        self.add_button.pack(pady=10)

        self.coches_listbox = tk.Listbox(self.frame, width=50)
        self.coches_listbox.pack()

        self.info_button = tk.Button(self.frame, text="Obtener Información", command=self.obtener_informacion)
        self.info_button.pack(pady=5)

        self.arrancar_button = tk.Button(self.frame, text="Arrancar", command=self.arrancar)
        self.arrancar_button.pack(pady=5)

        self.detener_button = tk.Button(self.frame, text="Detener", command=self.detener)
        self.detener_button.pack(pady=5)

    def añadir_coche(self):
        marca = self.marca_entry.get()
        modelo = self.modelo_entry.get()
        año = self.año_entry.get()
        coche = Coche(marca, modelo, año)
        self.coches.append(coche)
        self.coches_listbox.insert(tk.END, coche.obtener_informacion())
        self.marca_entry.delete(0, tk.END)
        self.modelo_entry.delete(0, tk.END)
        self.año_entry.delete(0, tk.END)

    def obtener_informacion(self):
        seleccion = self.coches_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            coche = self.coches[index]
            messagebox.showinfo("Información del Coche", coche.obtener_informacion())
        else:
            messagebox.showwarning("Advertencia", "Seleccione un coche de la lista")

    def arrancar(self):
        seleccion = self.coches_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            coche = self.coches[index]
            messagebox.showinfo("Arrancar Coche", coche.arrancar())
        else:
            messagebox.showwarning("Advertencia", "Seleccione un coche de la lista")

    def detener(self):
        seleccion = self.coches_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            coche = self.coches[index]
            messagebox.showinfo("Detener Coche", coche.detener())
        else:
            messagebox.showwarning("Advertencia", "Seleccione un coche de la lista")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30

