# temperatura.py

import tkinter as tk

# Función para convertir de grados Celsius a  Fahrenheit
def celsius_a_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    except ValueError:
        result_label.config(text="Entrada Invalida")

# Función para convertir de grados Fahrenheit a Celsius
def fahrenheit_a_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        result_label.config(text=f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Entrada Invalida")

# Creando la ventana principal
principal = tk.Tk()
principal.geometry("500x250")  # Ajusta el tamaño de la ventana
principal.title("Conversor Térmico")

# Conversión de grados Celcius a Fahrenheit 
celsius_label = tk.Label(principal, text="Ingrese Celsius:")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(principal)
celsius_entry.grid(row=0, column=1)

c_to_f_button = tk.Button(principal, text="Convierte a Fahrenheit", command=celsius_a_fahrenheit)
c_to_f_button.grid(row=0, column=2)

# Conversión de Grados Fahrenheit a Celsius 
fahrenheit_label = tk.Label(principal, text="Ingrese Fahrenheit:")
fahrenheit_label.grid(row=1, column=0)

fahrenheit_entry = tk.Entry(principal)
fahrenheit_entry.grid(row=1, column=1)

f_to_c_button = tk.Button(principal, text="Convierte a Celsius", command=fahrenheit_a_celsius)
f_to_c_button.grid(row=1, column=2)

# Muestra los resultados
result_label = tk.Label(
        principal, text="", font=("Helvetica", 18), bg="lightblue", height=3, width=30, bd=3, 
        cursor="hand2", fg="red",  padx=15, pady=15, justify=tk.CENTER, relief=tk.RAISED, 
        wraplength=250  )
result_label.grid(row=2, columnspan=3)

# relief=tk.RAISED
# Iniciar el bucle de eventos de Tkinter
principal.mainloop()


# REFERENCIA
# Oscar Núñez Mori. Jaén, Perú.  21-Jul-2024. Basado en:
# - w3resource (2023, Set 13).  Create a temperature converter in Python using Tkinter
#   https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-15.php

