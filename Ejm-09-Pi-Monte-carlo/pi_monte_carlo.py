# pi_monte_carlo.py
#
# Metodo Monte Carlo para encontrar pi.
import random # libreria de números aleatorios

def pi_estimado( num_muestras ):
    circulo_interior = 0

    for _ in range( num_muestras ):
        x = random.random()
        y = random.random()
        distancia = x ** 2 + y ** 2
        if distancia <= 1:
            circulo_interior += 1

    return ( circulo_interior / num_muestras ) * 4

# Numero de muestras aleatorias para la estimación
num_muestras = 10000000
pi_estimado = pi_estimado( num_muestras )
print("  ")
print( f"Valor estimado de pi depués de {num_muestras} muestras: {pi_estimado}" )

# Oscar Núñez Mori. Jaén, Perú. 21-Jul-2024. Basado en:
#    Pustam Raut (@pustam_egr) (s.f.). Pi using Monte Carlo method. 
#    https://www.mycompiler.io/view/KHbP70vHDpm


