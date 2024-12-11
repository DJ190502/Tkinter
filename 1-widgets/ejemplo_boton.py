import random
import time
import tkinter as tk
import os

ventana = tk.Tk()
ventana.title("Ejemplo de Label")
ventana.geometry("800x600+280+50")
ventana.configure(bg="gray")

boton = tk.Button(ventana, text="Presiona aqui")# Creacion del boton
boton.configure(fg="white", bg="green", font=("Arial",12)) # Personalizacion
boton.pack()

frame =tk.Frame(ventana)
frame.configure(width=700, height=400, bg="blue", bd=5,)
frame.pack_propagate(False)# No deja que el label redimensione el frame
frame.pack()

label = tk.Label(frame, text="Aqui")
label.pack()

def boton_presionado():
    palabras = ["Hola, que tal", "Que hay de nuevo", "Dios guiame"]
    ran_num = random.uniform(0,3)
    label.configure(text=palabras[int(ran_num)])

boton.config(command=boton_presionado)

ventana.mainloop()