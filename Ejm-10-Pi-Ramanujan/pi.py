# pi.py
# Estimanción de pi basado en:
# la fórmula de Ramanujan y el algoritmo de Chudnovsky

import math

def pi_ramanujan(iteraciones):
    # Inicializa la suma
    sum_term = 0.0

    # Realiza la sumatoria
    for k in range(iteraciones):
        term1 = math.factorial(4 * k) * (1103 + 26390 * k)
        term2 = (math.factorial(k) ** 4) * (396 ** (4 * k))
        sum_term += term1 / term2

    # Calcula el reciproco de la suma
    reciproco_sum = 2 * math.sqrt(2) / 9801 * sum_term

    # Estimación de pi
    pi_estimado = 1 / reciproco_sum

    return pi_estimado

def pi_chudnovsky(iteraciones):
    sum_term = 0
    for k in range(iteraciones):
        numerador    = ((-1) ** k) * math.factorial(6 * k) * (13591409+545140134*k)
        denominador  = math.factorial(3 * k) * (math.factorial(k) ** 3) * (640320 ** (3 * k))
        sum_term    += numerador / denominador
        total_sum    = math.sqrt(10005)/4270934400 * sum_term
    return 1/total_sum

# Numero de iteraciones para la aproximación 
iteraciones = 10

# Calcula  el valor estimado de pi
pi_r  = pi_ramanujan(iteraciones)
pi_c  = pi_chudnovsky(iteraciones)

# Compara con el valor actual de pi
# pi_actual = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
pi_actual = math.pi

print("")
print(f"PI estimado  (Ramanujan)  :", "%.50f" % pi_r)
print(f"PI estimado  (Chudnovsky) :", "%.50f" % pi_c)
print(f"PI actual    (aprox.)     :", "%.50f" % pi_actual)

# REFERENCIA
# Oscar Núñez Mori. Jaén, Perú. 21-Jul.-2024. Basado en:
# - Pustam Raut (@pustam_egr) (s.f.). Pi using Ramanujan's formula and Chudnovsky algorithm.
#   https://www.mycompiler.io/view/EaUqvGDExgh


