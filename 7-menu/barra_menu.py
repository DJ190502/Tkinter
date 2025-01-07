import tkinter as tk

ventana = tk.Tk()

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

archivo_menu = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=archivo_menu)


#def abrir_archivo():
#    print("Archivo Abierto")

#menu.add_command(label="Abrir", command=abrir_archivo)

ventana.mainloop()

#menu.add_command(label="Abrir")
#menu.add_command(label="Guardar")
