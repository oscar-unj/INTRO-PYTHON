# astronauta.py

class Astronauta:
    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia

    def __str__(self):
        return f"Astronauta: {self.nombre}, Rol: {self.rol}, Experiencia: {self.experiencia} años"


class Modulo:
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad

    def __str__(self):
        return f"Módulo: {self.nombre}, Tipo: {self.tipo}, Capacidad: {self.capacidad} personas"


class Mision:
    def __init__(self, nombre, objetivo):
        self.nombre = nombre
        self.objetivo = objetivo
        self.astronautas = []

    def asignar_astronauta(self, astronauta):
        self.astronautas.append(astronauta)
        print(f"Astronauta {astronauta.nombre} asignado a la misión '{self.nombre}'.")

    def __str__(self):
        astronautas = ', '.join([astronauta.nombre for astronauta in self.astronautas]) or "ninguno"
        return f"Misión: {self.nombre}, Objetivo: {self.objetivo}, Astronautas: {astronautas}"


class EstacionEspacial:
    def __init__(self, nombre):
        self.nombre = nombre
        self.modulos = []
        self.astronautas = []

    def añadir_modulo(self, modulo):
        self.modulos.append(modulo)
        print(f"Módulo '{modulo.nombre}' añadido a la estación espacial.")

    def registrar_astronauta(self, astronauta):
        self.astronautas.append(astronauta)
        print(f"Astronauta '{astronauta.nombre}' registrado en la estación espacial.")

    def mostrar_modulos(self):
        print(f"\nMódulos en la estación espacial '{self.nombre}':")
        for modulo in self.modulos:
            print(modulo)

    def mostrar_astronautas(self):
        print(f"\nAstronautas en la estación espacial '{self.nombre}':")
        for astronauta in self.astronautas:
            print(astronauta)


class ControlDeMision:
    def __init__(self):
        self.misiones = []

    def crear_mision(self, mision):
        self.misiones.append(mision)
        print(f"Misión '{mision.nombre}' creada con objetivo: '{mision.objetivo}'.")

    def asignar_astronauta_a_mision(self, mision, astronauta):
        mision.asignar_astronauta(astronauta)

    def generar_reporte_misiones(self):
        print("\nReporte de Misiones:")
        for mision in self.misiones:
            print(mision)


# Crear la estación espacial
estacion = EstacionEspacial("Internacional")

# Crear y añadir módulos a la estación espacial
modulo1 = Modulo("Laboratorio de Investigación", "Ciencia", 5)
modulo2 = Modulo("Módulo de Vivienda", "Habitación", 10)
modulo3 = Modulo("Módulo de Energía", "Energía", 2)

estacion.añadir_modulo(modulo1)
estacion.añadir_modulo(modulo2)
estacion.añadir_modulo(modulo3)

# Mostrar módulos de la estación espacial
estacion.mostrar_modulos()

# Registrar astronautas
astronauta1 = Astronauta("Alice", "Comandante", 15)
astronauta2 = Astronauta("Bob", "Ingeniero", 10)
astronauta3 = Astronauta("Charlie", "Científico", 8)

estacion.registrar_astronauta(astronauta1)
estacion.registrar_astronauta(astronauta2)
estacion.registrar_astronauta(astronauta3)

# Mostrar astronautas de la estación espacial
estacion.mostrar_astronautas()

# Crear el control de misión
control_de_mision = ControlDeMision()

# Crear y asignar astronautas a misiones
mision1 = Mision("Exploración Lunar", "Recolectar muestras de suelo lunar")
mision2 = Mision("Reparación de Satélite", "Reparar el satélite de comunicaciones")

control_de_mision.crear_mision(mision1)
control_de_mision.crear_mision(mision2)

control_de_mision.asignar_astronauta_a_mision(mision1, astronauta1)
control_de_mision.asignar_astronauta_a_mision(mision1, astronauta3)
control_de_mision.asignar_astronauta_a_mision(mision2, astronauta2)

# Generar reporte de misiones
control_de_mision.generar_reporte_misiones()

# OpenAI(2024). ChatGPT (Ver. Jul 23) [Programa en Python 3].
# https://chatgpt.com/share/d651cbb9-4992-4f48-a7b7-22bbe531dc30
