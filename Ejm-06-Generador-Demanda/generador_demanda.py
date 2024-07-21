# generador_demanda.py  
# Generador de Datos ficticios de Demanda Residencial de Energ. Eléctrica
# instalar los paquetes pandas y numpy
# pip install pandas
# pip install numpy

import pandas as pd
import numpy as np

# Generar datos simulados
np.random.seed(42)
timestamps = pd.date_range(start='2023-01-01', periods=10000, freq='H')


# consumo promedio de 5 kWh con desviación estándar de 2
consumo_kWh = np.random.normal(loc=5, scale=2, size=10000) 

# precio por kWh entre 0.10 y 0.20
precio_kWh = np.random.uniform(low=0.10, high=0.20, size=10000) 

# Crear DataFrame
data = pd.DataFrame({
    'timestamp': timestamps,
    'consumo_kWh': consumo_kWh,
    'precio_kWh': precio_kWh
})

# Guardar en un archivo CSV
data.to_csv('demanda_residencial.csv', index=False)

# REFERENCIA
# OpenAI(2024). ChatGPT (Ver. 20 Jul) [Estadísticas Demanda Energía].  
# https://chatgpt.com/share/daa2b9a7-3024-454b-90e7-0e0a8ba7c76b


