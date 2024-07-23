# equipo.py

import tkinter as tk
from tkinter import ttk
import csv

# Crear el archivo CSV
def crear_csv():
    with open('informacion_de_equipo.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'Rol', 'Correo'])
        writer.writerow(['Ana', 'Desarrolladora', 'ana@example.com'])
        writer.writerow(['Luis', 'Administrador', 'luis@example.com'])
        writer.writerow(['Carlos', 'Soporte', 'carlos@example.com'])
        writer.writerow(['María', 'Gerente', 'maria@example.com'])

# Leer el archivo CSV y devolver los datos como una lista de listas
def leer_csv():
    datos = []
    with open('informacion_de_equipo.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            datos.append(row)
    return datos

# Crear la GUI
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Información del Equipo")
        self.geometry("400x200")
        self.crear_interfaz()

    def crear_interfaz(self):
        cols = ('Nombre', 'Rol', 'Correo')
        self.tree = ttk.Treeview(self, columns=cols, show='headings')

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.grid(row=0, column=0, columnspan=2)
            self.tree.column(col, width=120)

        self.tree.grid(row=1, column=0, columnspan=2)

        datos = leer_csv()
        for dato in datos:
            self.tree.insert("", "end", values=dato)

        cerrar_btn = ttk.Button(self, text="Cerrar", command=self.destroy)
        cerrar_btn.grid(row=2, column=1)

if __name__ == "__main__":
    crear_csv()
    app = Aplicacion()
    app.mainloop()

# OpenAI(2024). ChatGPT (Ver. 23 Jul)[Procesar CSV con Tkinter]
# https://chatgpt.com/share/2225b69f-b9fb-465f-b0f6-dac78442b60c


