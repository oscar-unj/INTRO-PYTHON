# fibonacci.py

# Solicitamos la posición de la serie hasta la que debemos calcular
pos = int(input('Escriba que posición quiere de la serie de Fibonacci: '))

# Preguntamos si se desea desarrollar la serie
ans = input('Desea ver el resultado de toda la serie? ( S/N ) : ')

# Inicializamos las variables
iniFibo = 0
finFibo = 1

# Comenzamos el ciclo de calculo de Fibonacci hasta la posición indicada
for x in range(0,pos):

    # Evaluamos las dos primeras posiciones de la serie
    if x == 0:
        finFibo = 0
    elif x == 1:
        finFibo = 1

    # Si acepto desarrollar la serie se imprime la posición y el valor correspondiente
    # La posicion se le suma 1 ya que el rango comienza en 0 y no en 1
    if ans =='S' or ans == 's' :
         print(f'Posicion: {x+1:>4} -- Valor en la serie de Fibonacci:  {finFibo:>10}  ')

    # Guardamos el valor final de la seria antes de actualizarlo
    sum = finFibo

    # Actualizamos los valores de acuerdo al algoritmo
    finFibo = finFibo + iniFibo
    iniFibo = finFibo - iniFibo

# Imprime el valor final de la serie, independientemente si se desarrollo la serie o no
print(f'\nPosición Final: {x+1:>4} -- Valor en la serie de Fibonacci:  {sum:>10}  ')

# REFERENCIA
# Sagaom (2022, jul 28). Sucesión de Fibonacci en Python.
# https://www.sagaom.com/sucesion-de-fibonacci-en-python/


