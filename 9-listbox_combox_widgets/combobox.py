import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Ejemplo de Combobox")

combobox = ttk.Combobox(ventana, width=30, font=("Arial", 12), foreground="blue", background="white")
combobox.pack()

elementos = ["Elemento 1", "Elemento 2", 'Elemento 3']
combobox["values"] = elementos
elementos.remove("Elemento 1")
combobox["values"] = elementos

indice = 1
nuevo_valor= "Elemento modificado"
elementos[indice] = nuevo_valor
combobox["values"] = elementos

def on_seleccionar(event):
    valor_seleccionado = combobox.get()
    print(f"Seleccionado: {valor_seleccionado}")

combobox.bind("<<ComboboxSelected>>", on_seleccionar)

def on_clic(event):
    print("Clic en el Combobox")

combobox.bind("<Button-1>", on_clic)

ventana.mainloop()
