# graficos_demanda.py
# Instalar Librerias
# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV con 9000 registros
data = pd.read_csv('demanda_residencial.csv')

# Configurar el estilo de los gráficos
sns.set(style="whitegrid")

# Crear un histograma del consumo de energía
plt.figure(figsize=(10, 6))
sns.histplot(data['consumo_kWh'], bins=50, kde=True, color='blue')
plt.title('Histograma del Consumo de Energía (kWh)')
plt.xlabel('Consumo (kWh)')
plt.ylabel('Frecuencia')
plt.savefig('histograma_consumo.png')
plt.show()

# Crear un boxplot del consumo de energía
plt.figure(figsize=(10, 6))
sns.boxplot(x=data['consumo_kWh'], color='green')
plt.title('Boxplot del Consumo de Energía (kWh)')
plt.xlabel('Consumo (kWh)')
plt.savefig('boxplot_consumo.png')
plt.show()

# Crear un gráfico de dispersión entre el consumo y el precio
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['consumo_kWh'], y=data['precio_kWh'], alpha=0.5)
plt.title('Gráfico de Dispersión entre Consumo y Precio')
plt.xlabel('Consumo (kWh)')
plt.ylabel('Precio (€/kWh)')
plt.savefig('scatter_consumo_precio.png')
plt.show()

# Calcular la matriz de correlación
correlation_matrix = data.corr()

# Crear un mapa de calor de la correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Mapa de Calor de la Correlación')
plt.savefig('heatmap_correlacion.png')
plt.show()

# REFERENCIA
# OpenAI (2024). ChatGPT (Ver. 20 Jul.)[Estadística Demanda Energía].
# https://chatgpt.com/share/daa2b9a7-3024-454b-90e7-0e0a8ba7c76b

