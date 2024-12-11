import tkinter as tk

ventana = tk.Tk()

#entero = tk.IntVar(value=42)
entero = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="Opcion 1", variable=entero, value=50)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="Opcion 2", variable=entero, value=60)
opcion2.pack()
label = tk.Label(ventana, text="Elija algun valor")#Valor por defecto
label.pack()

def actualizar(*args): #Funcion para actualizar le valor del label
    label.config(text=entero.get())

entero.trace("w", actualizar)#Para trazear los cambios

ventana.mainloop()
