# control_y_bucles.py

# 1. condicional if
print("")
num_ent = int(input("Ingresa un número entero: "))
print("")
if num_ent > 0:
    print("El número es positivo")
print("")

# 2. condicional if else
num = 10
if num > 0:
    print(f"El número {num} es positivo \n")
else:
    print(f"El número {num} es negativo \n")

# 3. Bucle for
maximo = 10
for numero in range(maximo):
    print(f"El número es: {numero}")
print("")

# 4. Bucle while
numeroDecimal = float(input("Ingresa un número entero menor que 10 : "))
while numeroDecimal < 10:
    print(f"El número es: {numeroDecimal}")
    numeroDecimal = numeroDecimal + 1
print("")


# 5. Python no cuenta con switch case, pero se puede hacer asi 

# 5.1 En forma númerica

edad = int(input("Que edad tiene: "))

if edad > 90:
    print("Estas muy viejito, Abuelito.\n")
elif edad < 0:
    print("Todavía no has nacido esperate un poco.\n")
elif edad >= 18:
    print("Ya puede ir a fiestas de mayores\n")
else:
    print("SSEres aún muy joven para la fiesta\n")

# 5.2 Como texto

lang = input("\n Ingresa el programa (JavaSCript, PHP, Python, Solidity, R): ").lower()

def switch(lang):
    if lang == "javascript":
        return "\n Puedes llegar a ser un Desarrollador Web con JavaScript.\n"
    elif lang == "php":
        return "\n Puedes llegar a ser un Desarrolador Backend con PHP.\n"
    elif lang == "python":
        return "\n Puedes llegar a ser un Cientifico de Datos con Python. \n"
    elif lang == "solidity":
        return "\n Puedes llegar a ser un Desarrolador de  Blockchain con Solidity.\n"
    elif lang == "r":
        return "\n Puedes llegar a ser un Excelente Estadistico con Lenguaje R.\n"

print(switch(lang))

# 5.3 usando match - case

lenguaje = input("\n ¿Que lenguaje de programación quieres aprender (Javascript, Python, PHP, Solidity, Java, R)?: ").lower()

match lenguaje:
    case "javascript":
        print("\n Puedes llegar a ser un Desarrollador Web con JavaScript.\n")

    case "python":
        print("\n Puedes llegar a ser un Científico de Datos con Python.\n")

    case "php":
        print("\n Puedes llegar a ser un Desarrollador Backend en PHP.\n")

    case "solidity":
        print("\n Puedes llegar a ser un desarrollador Blockchain.\n")

    case "java":
        print("\n Puedes llegar a ser un desarrollador de aplicaciones moviles con Java.\n")

    case "r":
        print("\n Puedes llegar a ser un Excelente Estadístico con Lengeaje R.\n")

    case _:
        print("\n El lenguaje no importa, lo que importa es solucionar los problemas.\n.")



# 6. Python no tiene bucle Do While pero se puede emular asi:

palabra_secreta = "python"
contador = 0

while True:
    palabra = input("Ingrese la palabra secreta: ").lower()
    contador = contador + 1
    if palabra == palabra_secreta:
        print("\n Bienvenido Amigo.")
        break
    if palabra != palabra_secreta and contador > 7:
        print("\n----------------------------------------------------------")
        print("¡Llamaremos a la policia digital, Ud. no esta autorizado!")
        break


# Oscar Núñez Mori. Jaén. Perú. 23-Jul-2024. Basado en:
# - Códigital (2023, Jun 26). Introducción a Python: 10 ejemplos de código para principiantes.
#   https://codigital.ec/introduccion-a-python-10-ejemplos-de-codigo-para-principiantes/
# - Dionysia Lemonaki (2021, Ago 31). Python Do While – Loop Example
#   https://www.freecodecamp.org/news/python-do-while-loop-example/
# - Kolade Chris (2022, Ago 5). Python Switch Statement – Switch Case.
#   https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
