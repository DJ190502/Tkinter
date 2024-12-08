import time
import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Label")

label = tk.Label(ventana, text= "Hola, soy un Label")
label.pack()

def actualizar_hora():
    label.config(text=time.strftime("%H:%M:%S"))# Me da la hora
    ventana.after(1000, actualizar_hora)#Actualiza el tiempo(after despues)

actualizar_hora()

ventana.mainloop()