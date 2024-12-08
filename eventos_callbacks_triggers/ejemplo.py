import tkinter as tk

def on_click(event):
    print(f"{event.widget['text']} presionado")

ventana = tk.Tk()

# Creamos una lista de botones utilizando una comprensión de lista
# Cada botón tendrá un texto que indica su número (Boton 0, Boton 1, Boton 2)
buttons = [tk.Button(ventana, text=f"Boton {i}") for i in range(3)]

# Iteramos sobre cada botón en la lista de botones
for button in buttons:
    button.pack()  # Añadimos el botón a la ventana (lo mostramos)
    button.bind("<Button-1>", on_click)  # Asociamos el evento de clic izquierdo del ratón a la función on_click

ventana.mainloop()