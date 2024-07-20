# ventana.py

from tkinter import *

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Hola mundo")

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    ventana.mainloop()

# REFERENCIA
# Programador Novato (s.f.). Hola Mundo con Python y TKinter.
# https://www.programadornovato.com/hola-mundo-con-python-y-tkinter/

