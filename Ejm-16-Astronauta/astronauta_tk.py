# astronauta_tk.py

import tkinter as tk
from tkinter import messagebox

class Astronauta:
    def __init__(self, nombre, edad, misiones):
        self.nombre = nombre
        self.edad = edad
        self.misiones = misiones

    def __str__(self):
        return f"{self.nombre}, Edad: {self.edad}, Misiones: {', '.join(self.misiones)}"

class ProgramaEspacial:
    def __init__(self, nombre):
        self.nombre = nombre
        self.astronautas = []

    def agregar_astronauta(self, astronauta):
        self.astronautas.append(astronauta)
        return f"Astronauta {astronauta.nombre} agregado al programa {self.nombre}."

    def mostrar_astronautas(self):
        if not self.astronautas:
            return "No hay astronautas en el programa."
        return "\n".join(str(astronauta) for astronauta in self.astronautas)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Astronautas")

        self.programa_espacial = ProgramaEspacial("Exploradores del Espacio")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Gestión de Astronautas", font=("Arial", 16))
        self.label.pack(pady=10)

        self.astronautas_label = tk.Label(self.frame, text="Astronautas")
        self.astronautas_label.pack()

        self.astronautas_text = tk.Text(self.frame, height=10, width=50)
        self.astronautas_text.pack()

        self.actualizar_button = tk.Button(self.frame, text="Actualizar", command=self.actualizar)
        self.actualizar_button.pack(pady=10)

        self.astronauta_label = tk.Label(self.frame, text="Añadir Astronauta (Nombre, Edad, Misiones):")
        self.astronauta_label.pack()
        self.astronauta_entry = tk.Entry(self.frame)
        self.astronauta_entry.pack()

        self.añadir_astronauta_button = tk.Button(self.frame, text="Añadir Astronauta", command=self.añadir_astronauta)
        self.añadir_astronauta_button.pack(pady=5)

        self.salir_button = tk.Button(self.frame, text="Salir", command=root.quit)
        self.salir_button.pack(pady=10)

    def actualizar(self):
        self.astronautas_text.delete(1.0, tk.END)
        self.astronautas_text.insert(tk.END, self.programa_espacial.mostrar_astronautas())

    def añadir_astronauta(self):
        datos = self.astronauta_entry.get().split(", ")
        if len(datos) >= 3:
            nombre = datos[0]
            try:
                edad = int(datos[1])
            except ValueError:
                messagebox.showwarning("Advertencia", "La edad debe ser un número.")
                return
            misiones = datos[2:]
            astronauta = Astronauta(nombre, edad, misiones)
            mensaje = self.programa_espacial.agregar_astronauta(astronauta)
            messagebox.showinfo("Añadir Astronauta", mensaje)
            self.astronauta_entry.delete(0, tk.END)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduzca los datos del astronauta en el formato correcto.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30

