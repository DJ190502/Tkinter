from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Ventana Principal")
ventana.geometry("600x400")

ventana_toplevel= Toplevel(ventana)
ventana_toplevel.geometry('300x300')
ventana_toplevel.title('TopLevel')
label = tk.Label(ventana_toplevel, text="Ventana TopLevel")
label.pack()

def cerrar_ventana_toplevel(ventana):
    ventana.destroy()# Para elminar una ventana

boton_cerrar = tk.Button(ventana, text="Cerrar Ventana top level", command=lambda: cerrar_ventana_toplevel(ventana_toplevel))
boton_cerrar.pack() # Si yo le quito a las funciones encargadas de escribir los números en la StringVar la función lambda,
# al momento de ejecutarse el programa ya aparecen escritos los números sin que
# yo presione los botones, en cambio con las funciones lambda espera a que yo presione el botón para escribir.
# https://es.stackoverflow.com/questions/270617/c%C3%B3mo-actuan-las-funciones-lambda-en-este-c%C3%B3digo
ventana.mainloop()


