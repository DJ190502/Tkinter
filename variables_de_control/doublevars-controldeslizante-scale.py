from math import pi
import tkinter as tk

ventana = tk.Tk()

decimal = tk.DoubleVar(value=pi)

control_deslizante = tk.Scale(ventana, variable=decimal, from_=0, to=10, resolution=0.01, orient=tk.HORIZONTAL)
#variable es valor que presenta el scale
#from_ te dice desde donde empieza los valores del scale
#to te dice hasta donde llega los valores del scale
#resolution te dice cuanto en cuanto el valor cambia en la escala por ejemplo empieza en 0 el siguein es 0.01
#orient es la orientacion de la barra

control_deslizante.pack()

ventana.mainloop()