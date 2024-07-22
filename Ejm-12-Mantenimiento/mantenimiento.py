# mantenimiento.py   

# pip install tk pandas numpy matplotlib seaborn  # instalar estas librerias
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Creación de la clase Mantenimiento
class Mantenimiento:
    def __init__(self, raiz):   
        self.raiz = raiz
        self.raiz.title("Mantenimiento Industrial - Planta Hidroeléctrica")
        # Botón de Carga de Archivo .csv
        self.load_button = tk.Button(raiz, text="Cargar Archivo CSV", command=self.load_file)
        self.load_button.pack()
        # Botón de cambio de imagen
        self.next_button = tk.Button(raiz, text="Siguiente", command=self.show_next_graph)
        self.next_button.pack()
        self.next_button.config(state=tk.DISABLED)
        # Botón para salir del programa
        self.quit_button = tk.Button(raiz, text="Terminar", command=raiz.quit)
        self.quit_button.pack()

        self.canvas = None
        self.graphs = []
        self.current_graph = 0

        # Configurar tamaño de la ventana
        self.raiz.geometry("1200x800")
    # Función para cargar el archivo .csv
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            data = pd.read_csv(file_path)
            self.prepare_graphs(data)
            self.current_graph = 0
            self.show_next_graph()
            self.next_button.config(state=tk.NORMAL)
    # Función para generar los gráficos del archivo .csv
    def prepare_graphs(self, data):
        self.graphs = []

        # Preparar primer gráfico (gráfico de series temporales)
        fig, ax = plt.subplots(figsize=(12, 8))
        data["Fecha"] = pd.to_datetime(data["Fecha"])
        data.set_index("Fecha", inplace=True)
        data.plot(ax=ax)
        self.graphs.append(fig)

        # Preparar segundo gráfico (mapa de calor de correlación)
        fig_corr, ax_corr = plt.subplots(figsize=(12, 8))
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax_corr)
        self.graphs.append(fig_corr)

        # Preparar tercer gráfico (gráfico de regresión)
        fig_reg, ax_reg = plt.subplots(figsize=(12, 8))
        sns.regplot(x=data['Horas_Operación'], y=data['Horas_Mantenimiento'], ax=ax_reg)
        self.graphs.append(fig_reg)
    # Función par mostrar los gráficos en la ventana
    def show_next_graph(self):
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()

        fig = self.graphs[self.current_graph]
        self.canvas = FigureCanvasTkAgg(fig, master=self.raiz)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        self.current_graph = (self.current_graph + 1) % len(self.graphs)

# Función Principal
if __name__ == "__main__":
    raiz = tk.Tk()
    aplicacion = Mantenimiento(raiz)
    raiz.mainloop()

# Oscar Núñez Mori. Jaén, Perú. 22-Jul-2024. Basado en: 
# - OpenAI (2024). ChatGPT (Ver. 21 Jul.) [Tkinter CSV Data Visualization].
#   https://chatgpt.com/share/d40d1ef5-1f12-4bcd-9ba3-040f993cb67c

