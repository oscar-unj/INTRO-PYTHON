# genera_csv.py

import pandas as pd
import numpy as np

# Número de datos
num_datos = 10000

# Generar fechas
fechas = pd.date_range(start='2024-01-01', periods=num_datos, freq='D')

# Generar datos aleatorios
horas_operacion = np.random.randint(100, 150, size=num_datos)
horas_mantenimiento = np.random.randint(3, 10, size=num_datos)
paradas_no_programadas = np.random.randint(0, 3, size=num_datos)

# Crear DataFrame
data = {
    "Fecha": fechas,
    "Horas_Operación": horas_operacion,
    "Horas_Mantenimiento": horas_mantenimiento,
    "Paradas_No_Programadas": paradas_no_programadas
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv("mantenimiento_industrial.csv", index=False)

print("Archivo mantenimiento_industrial.csv generado con 10,000 datos.")


# REFERENCIA
# OpenAI(2024). ChatGPT (Ver. 20 jul.)[Tkinter CSV Data Visualization].
# https://chatgpt.com/share/d40d1ef5-1f12-4bcd-9ba3-040f993cb67c

