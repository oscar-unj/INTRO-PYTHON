# mensaje.py

from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text ='JAÉN', font = "50")
w.pack()

msg = Message( root, text = "Ingeniería para Todos")

msg.pack()

root.mainloop()

# Oscar Núñez Mori. Jaén 20-Jul-2024. Basado en:
#  - Geeks for Geeks (2020). Python Tkinter - Message
#    https://www.geeksforgeeks.org/python-tkinter-message/


