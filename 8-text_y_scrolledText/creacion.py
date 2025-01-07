import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ventana = tk.Tk()
texto = tk.Text(ventana, width=40, height=10, wrap="word", bg='lightgray', fg="black", padx='10', pady='10', font=("Helvetica", 12))

texto.insert("1.0", "¡Bienvenido a nuestro editor de texto!")
texto.insert("end","\n\nEste es un ejemplo de texto resaltado", "resaltado")
texto.tag_config("resaltado", background="yellow", foreground="black")
contenido = texto.get("1.0", "end")
texto.delete("1.0", "end")
print(contenido)
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