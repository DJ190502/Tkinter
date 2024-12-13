import tkinter as tk

ventana = tk.Tk()

boolean = tk.BooleanVar(value=True)

casilla = tk.Checkbutton(ventana, text="Aceptar", variable=boolean)
casilla.pack()

def actualizar(*args):
    print(boolean.get())

boolean.trace("w", actualizar)

ventana.mainloop()