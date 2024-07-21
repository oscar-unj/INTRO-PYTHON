# ec_2do.py

from math import sqrt

# mostramos un mensaje de bienvenida
print('¡Hola! Vamos a resolver una ecuación de segundo grado:')
print('    ax² + bx + c = 0\n')

# pedimos los coeficientes al usuario
a, b, c = [float(input(f'Dame el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]

# calculamos el discriminante
discriminante =  b * b - 4 * a * c

if discriminante < 0: # comprobamos si no existen soluciones reales
    print(f'La ecuación no tiene soluciones reales.')
else:
    raiz = sqrt(discriminante)      # calculamos la raíz
    x_1 = (-b + raiz) / (2 * a)     # calculamos una primera solución
    if discriminante != 0:          # comprobamos si hay otra solución
        x_2 = (-b - raiz) / (2 * a) # calculamos la segunda solución
        print(f'Las soluciones son {x_1} y {x_2}.') # mostramos las dos soluciones
    else:
        print(f'La única solución es x = {x_1}') # mostramos la única solución


# REFERENCIA
# Código Pitón (2024). Cómo Resolver Ecuaciones de Segundo Grado en Python.
# https://www.codigopiton.com/resolver-ecuaciones-de-segundo-grado-en-python/



