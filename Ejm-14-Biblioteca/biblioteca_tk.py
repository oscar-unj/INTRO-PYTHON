# biblioteca_tk.py

import tkinter as tk
from tkinter import messagebox

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - {estado}"

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            return f"{self.nombre} ha tomado prestado '{libro.titulo}'."
        else:
            return f"Lo siento, '{libro.titulo}' no está disponible."

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            return f"{self.nombre} ha devuelto '{libro.titulo}'."
        else:
            return f"{self.nombre} no tiene '{libro.titulo}' prestado."

    def __str__(self):
        libros = ', '.join([libro.titulo for libro in self.libros_prestados]) or "ninguno"
        return f"Miembro: {self.nombre}, Libros prestados: {libros}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def añadir_libro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' añadido a la biblioteca."

    def registrar_miembro(self, miembro):
        self.miembros.append(miembro)
        return f"Miembro '{miembro.nombre}' registrado en la biblioteca."

    def mostrar_libros(self):
        return "\n".join(str(libro) for libro in self.libros)

    def mostrar_miembros(self):
        return "\n".join(str(miembro) for miembro in self.miembros)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Biblioteca")

        self.biblioteca = Biblioteca()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Gestión de Biblioteca", font=("Arial", 16))
        self.label.pack(pady=10)

        self.libros_label = tk.Label(self.frame, text="Libros")
        self.libros_label.pack()

        self.libros_text = tk.Text(self.frame, height=10, width=50)
        self.libros_text.pack()

        self.miembros_label = tk.Label(self.frame, text="Miembros")
        self.miembros_label.pack()

        self.miembros_text = tk.Text(self.frame, height=10, width=50)
        self.miembros_text.pack()

        self.actualizar_button = tk.Button(self.frame, text="Actualizar", command=self.actualizar)
        self.actualizar_button.pack(pady=10)

        self.libro_label = tk.Label(self.frame, text="Añadir Libro (Titulo, Autor, ISBN):")
        self.libro_label.pack()
        self.libro_entry = tk.Entry(self.frame)
        self.libro_entry.pack()

        self.añadir_libro_button = tk.Button(self.frame, text="Añadir Libro", command=self.añadir_libro)
        self.añadir_libro_button.pack(pady=5)

        self.miembro_label = tk.Label(self.frame, text="Registrar Miembro (Nombre):")
        self.miembro_label.pack()
        self.miembro_entry = tk.Entry(self.frame)
        self.miembro_entry.pack()

        self.registrar_miembro_button = tk.Button(self.frame, text="Registrar Miembro", command=self.registrar_miembro)
        self.registrar_miembro_button.pack(pady=5)

        self.nombre_miembro_label = tk.Label(self.frame, text="Nombre del Miembro:")
        self.nombre_miembro_label.pack()
        self.nombre_miembro_entry = tk.Entry(self.frame)
        self.nombre_miembro_entry.pack()

        self.libro_prestado_label = tk.Label(self.frame, text="Título del Libro:")
        self.libro_prestado_label.pack()
        self.libro_prestado_entry = tk.Entry(self.frame)
        self.libro_prestado_entry.pack()

        self.tomar_prestado_button = tk.Button(self.frame, text="Tomar Prestado", command=self.tomar_prestado)
        self.tomar_prestado_button.pack(pady=5)

        self.devolver_libro_button = tk.Button(self.frame, text="Devolver Libro", command=self.devolver_libro)
        self.devolver_libro_button.pack(pady=5)

        self.salir_button = tk.Button(self.frame, text="Salir", command=root.quit)
        self.salir_button.pack(pady=10)

    def actualizar(self):
        self.libros_text.delete(1.0, tk.END)
        self.libros_text.insert(tk.END, self.biblioteca.mostrar_libros())

        self.miembros_text.delete(1.0, tk.END)
        self.miembros_text.insert(tk.END, self.biblioteca.mostrar_miembros())

    def añadir_libro(self):
        datos = self.libro_entry.get().split(", ")
        if len(datos) == 3:
            libro = Libro(datos[0], datos[1], datos[2])
            mensaje = self.biblioteca.añadir_libro(libro)
            messagebox.showinfo("Añadir Libro", mensaje)
            self.libro_entry.delete(0, tk.END)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduzca los datos del libro en el formato correcto.")

    def registrar_miembro(self):
        nombre = self.miembro_entry.get()
        if nombre:
            miembro = Miembro(nombre)
            mensaje = self.biblioteca.registrar_miembro(miembro)
            messagebox.showinfo("Registrar Miembro", mensaje)
            self.miembro_entry.delete(0, tk.END)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduzca el nombre del miembro.")

    def tomar_prestado(self):
        nombre_miembro = self.nombre_miembro_entry.get()
        titulo_libro = self.libro_prestado_entry.get()

        miembro = next((m for m in self.biblioteca.miembros if m.nombre == nombre_miembro), None)
        libro = next((l for l in self.biblioteca.libros if l.titulo == titulo_libro), None)

        if miembro and libro:
            mensaje = miembro.tomar_prestado(libro)
            messagebox.showinfo("Tomar Prestado", mensaje)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "Miembro o libro no encontrado.")

    def devolver_libro(self):
        nombre_miembro = self.nombre_miembro_entry.get()
        titulo_libro = self.libro_prestado_entry.get()

        miembro = next((m for m in self.biblioteca.miembros if m.nombre == nombre_miembro), None)
        libro = next((l for l in self.biblioteca.libros if l.titulo == titulo_libro), None)

        if miembro and libro:
            mensaje = miembro.devolver_libro(libro)
            messagebox.showinfo("Devolver Libro", mensaje)
            self.actualizar()
        else:
            messagebox.showwarning("Advertencia", "Miembro o libro no encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30

