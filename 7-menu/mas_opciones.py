import tkinter as tk

ventana = tk.Tk()

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)

def abrir_archivo():
   print("Archivo Abierto")

archivo_menu.add_command(label='Nuevo')
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_separator() # Separa
archivo_menu.add_command(label="Salir")

#Agrega un menu editar a la barra de menu

editar_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Editar", menu=editar_menu)

editar_menu.add_command(label='Deshacer')
editar_menu.add_command(label="Rehacer")

ventana.mainloop()
