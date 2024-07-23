# operaciones.py

# 1. Bienvenidos
print("")
print("Bienvenidos Chicos, con python se divertirán")
print("")

# 2. Operaciones matemáticas

# 2.1 Suma
a = 10
b = 20
suma = a + b
print(f"La suma de {a} + {b} es: {suma}")
print(suma)
print("")

# 2.2 Resta
c = 45
d = 25
resta = c - d

print(f"La resta de {c} - {d} es: {resta}")
print(resta)
print("")

# 2.3 Multiplicación
e = 25
f = 3
multiplicacion = e * f
print(f"La multiplicacion  de {e} * {f} es: {multiplicacion}")
print(multiplicacion)
print("")

# 2.4 División
g = 11
h = 2
division = g / h
print(f"La división  de {g} / {h} es: {division} \n")

# 2.5 Resto
i = 11
j = 2
resto = i % j
print(f"El Resto de dividir {i} entre {h} es: {resto} \n")

# 2.6 Potencia
k = 2
l = 5
potencia = k**l
print(f"La  potencia de {k} elevado {l} es: {potencia} \n")

# 2.7 Raiz cuadrada
# Importamos la función math
from math import sqrt
# ingresamos un número por el terminal
num = float(input("Ingrese un número para hallar su raiz cuadrada: "))
# Calculamos su raíz
raiz = sqrt(num)
print(f"La raiz cuadrada del número {num} es {raiz} \n")

# 2.8 Raiz cubica 
# ingresamos un número por el terminal
numero = float(input("Ingrese un número para hallar su raiz cúbica: "))
# Calculamos su raíz cúbica
raiz_cub = numero ** (1/3)

print(f"La raiz cúbica  del número {numero} es {raiz_cub} \n")

# 3. Variables y tipos de datos
nombre = "Oscar"
edad = 54
altura = 1.75
es_profesor = True
print(f"nombre: {nombre}, edad: {edad}, altura: {altura}, es profesor: {es_profesor} \n")
print(nombre, edad, altura, es_profesor)
print("")

# 4. Listas
vegetales = ["zanahoria", "lechuga", "pepino", "tomate"]
print(vegetales)
print("")

# 4.1 Acceder a un elemento de la lista
print("Acceder a un elemento de la lista: \n")
print(vegetales[0])
print("")

# 4.2 Agregar un elemento a la lista
print("Agregar un elemnto a la lista: \n")
vegetales.append("apio")
print(vegetales)
print("")

# 4.3 Longitud de la lista
print("La longitud de la lista es: \n")
print(len(vegetales))
print("")

# Oscar Núñez Mori. Jaén. Perú. 23-Jul-2024. Basado en:
# - Códigital (2023, Jun 26). Introducción a Python: 10 ejemplos de código para principiantes. 
#   https://codigital.ec/introduccion-a-python-10-ejemplos-de-codigo-para-principiantes/
# - Bilateria (2024). Lenguaje de Programación Python: sqrt
#   https://python.bilateria.org/sqrt.html
