import tkinter as tk

ventana = tk.Tk()
#imagen = tk.PhotoImage(file="Ruta")//Aqui iria la foto en cualquiera menos jpg
#imagen2 = tk.PhotoImage(file="Ruta")//Aqui iria la foto en cualquiera menos jpg

etiqueta = tk.Label(ventana, image=imagen)
boton = tk.Button(ventana, image=imagen2)
etiqueta.pack()
boton.pack()

ventana.mainloop()