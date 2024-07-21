# estadistica_demanda.py
# debes tener la libreria de  pandas
# pip install pandas

import pandas as pd

# Leer el archivo CSV con 9000 registros
data = pd.read_csv('demanda_residencial.csv')

# Calcular estadísticas básicas
estadisticas = data.describe()

# Calcular la mediana
mediana_consumo = data['consumo_kWh'].median()
mediana_precio  = data['precio_kWh'].median()

# Calcular la moda
moda_consumo = data['consumo_kWh'].mode()[0]
moda_precio  = data['precio_kWh'].mode()[0]

# Calcular la correlación de Pearson y Spearman
correlacion_pearson  = data['consumo_kWh'].corr(data['precio_kWh'], method='pearson')
correlacion_spearman = data['consumo_kWh'].corr(data['precio_kWh'], method='spearman')

# Resultados
print("Estadísticas Descriptivas:\n", estadisticas)
print("\nMediana del Consumo (kWh):", mediana_consumo)
print("Mediana del Precio (kWh):"   , mediana_precio)
print("\nModa del Consumo (kWh):"   , moda_consumo)
print("Moda del Precio (kWh):"      , moda_precio)
print("\nCorrelación de Pearson:"   , correlacion_pearson)
print("Correlación de Spearman:"    , correlacion_spearman)

# REFERENCIA
# OpenAI (2024). ChatGPT (Ver. 20 Jul.)[Estadística Demanda Energía].
# https://chatgpt.com/share/daa2b9a7-3024-454b-90e7-0e0a8ba7c76b


