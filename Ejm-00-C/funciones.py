# funciones.py

# 1. Función suma.

a = float(input("Ingresa un número: "))
b = float(input("Ingresa otro número: "))

def suma(a, b):
    return a + b

resultado = suma(a, b)

print(f"\n la suma de {a} + {b} es {resultado}\n")

# 2. Función Recursiva

numero = float(input("Ingresa un número: "))

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

resultado = factorial_recursivo(numero) # 120

print(f"\n El factorial de {numero} es: {resultado} \n")

# 3. Lectura y Escritura de Archivos.

# Abrir archivo mis_datos.txt para escribir
archivo = open("mis_datos.txt", "w")
archivo.write("Archivo para guardar datos experimentales")
archivo.close()

# Abrir archivo para leer de mis_datos.txt
print("Contenido del archivo: \n")
archivo = open("mis_datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# 4. Módulos
import random
numero_aleatorio = random.randint(1, 100)
print("\nEl número aleatorio es: {numero_aleatorio}\n")
 
# 5. Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: división por cero")


# Oscar Núñez Mori. Jaén. Perú. 23-Jul-2024. Basado en:
# - Códigital (2023, Jun 26). Introducción a Python: 10 ejemplos de código para principiantes.
#   https://codigital.ec/introduccion-a-python-10-ejemplos-de-codigo-para-principiantes/
# - El Libro de Python (2024). Recursividad
#   https://ellibrodepython.com/recursividad

