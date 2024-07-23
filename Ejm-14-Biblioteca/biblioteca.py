# biblioteca.py

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
            print(f"{self.nombre} ha tomado prestado '{libro.titulo}'.")
        else:
            print(f"Lo siento, '{libro.titulo}' no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no tiene '{libro.titulo}' prestado.")

    def __str__(self):
        libros = ', '.join([libro.titulo for libro in self.libros_prestados]) or "ninguno"
        return f"Miembro: {self.nombre}, Libros prestados: {libros}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def añadir_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def registrar_miembro(self, miembro):
        self.miembros.append(miembro)
        print(f"Miembro '{miembro.nombre}' registrado en la biblioteca.")

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

    def mostrar_miembros(self):
        for miembro in self.miembros:
            print(miembro)


# Crear instancias de Libro
libro1 = Libro("1984", "George Orwell", "1234567890")
libro2 = Libro("To Kill a Mockingbird", "Harper Lee", "0987654321")

# Crear instancia de Biblioteca
biblioteca = Biblioteca()

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear instancias de Miembro
miembro1 = Miembro("Alice")
miembro2 = Miembro("Bob")

# Registrar miembros en la biblioteca
biblioteca.registrar_miembro(miembro1)
biblioteca.registrar_miembro(miembro2)

# Mostrar libros y miembros
print("\nLibros en la biblioteca:")
biblioteca.mostrar_libros()

print("\nMiembros de la biblioteca:")
biblioteca.mostrar_miembros()

# Tomar prestado y devolver libros
miembro1.tomar_prestado(libro1)
miembro1.devolver_libro(libro1)
miembro2.tomar_prestado(libro2)
miembro2.devolver_libro(libro1)  # Este intento debería fallar

# Mostrar el estado final de los libros y miembros
print("\nEstado final de los libros:")
biblioteca.mostrar_libros()

print("\nEstado final de los miembros:")
biblioteca.mostrar_miembros()

# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30


