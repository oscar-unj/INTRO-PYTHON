# coche.py
# Ejemplo de python con clases.

class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    def arrancar(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.modelo} está ahora encendido.")
        else:
            print(f"El {self.modelo} ya está encendido.")

    def detener(self):
        if self.encendido:
            self.encendido = False
            print(f"El {self.modelo} está ahora apagado.")
        else:
            print(f"El {self.modelo} ya está apagado.")

    def obtener_informacion(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

# Crear instancias de la clase Coche
coche1 = Coche("Toyota", "Corolla", 2020)
coche2 = Coche("Ford", "Mustang", 1967)

# Usar métodos de las instancias
print(coche1.obtener_informacion())
coche1.arrancar()
coche1.detener()

print(coche2.obtener_informacion())
coche2.arrancar()
coche2.detener()

# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30


