from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Ventana Principal")
ventana.geometry("600x400")

def abrir_ventana_toplevel():
    ventana_toplevel= Toplevel(ventana)
    ventana_toplevel.geometry('300x300')
    ventana_toplevel.title('TopLevel')
    label = tk.Label(ventana_toplevel, text="Ventana TopLevel")
    label.pack()

boton = Button(ventana, text="Abrir Ventana Toplevel", command=abrir_ventana_toplevel)
boton.pack()

def cerrar_ventana_toplevel(ventana):
    ventana.destroy()

boton_cerrar = tk.Button(ventana, text="Cerrar Ventana top level", command=lambda )

ventana.mainloop()
