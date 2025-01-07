import tkinter as tk

ventana = tk.Tk()

menubutton = tk.Menubutton(ventana, text="Archivo")
menubutton.pack()

menu = tk.Menu(menubutton)
menubutton.config(menu=menu)

menu.add_command(label="Abrir")
menu.add_command(label="Guardar")


ventana.mainloop()