import tkinter as tk

ventana = tk.Tk()

#entero = tk.IntVar(value=42)
entero = tk.IntVar()

casilla = tk.Checkbutton(ventana, text="Aceptar", variable=entero, onvalue=1, offvalue=0)
#onvalue es el valor cuando esta presionado, offvaule es cuando no esta puesto
casilla.pack()

label = tk.Label(ventana, text="")#Valor por defecto
label.pack()


def actualizar(*args):
    label.config(text=entero.get())

entero.trace("w", actualizar)

ventana.mainloop()