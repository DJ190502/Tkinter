import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
texto = tk.Text(ventana)

texto.pack()

texto_desplazable = ScrolledText(ventana)
texto_desplazable.pack()

ventana.mainloop()

"""
def mostrar_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root, event.y_root)

menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label="Copiar")
menu_contextual.add_command(label="Pegar")

ventana.bind("<Button-3>", mostrar_menu_contextual)

ventana.mainloop()
"""