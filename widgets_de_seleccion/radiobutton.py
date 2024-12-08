import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo RadioButton")

variable_control = tk.IntVar()#Guardara el valor que esta marcado

'''
def mostrar_seleccion():
    print(f"Opcion seleccion: {variable_control.get()}")#Muestra el valor elegido

boton = tk.Button(ventana, text='Mostrar Seleccion', command=mostrar_seleccion)
boton.pack()'''

'''
def cambiar_color():
    if variable_control.get() == 1:
        ventana.config(bg='blue')
    elif variable_control.get() == 2:
        ventana.config(bg='red')

boton = tk.Button(ventana, text='Cambiar Background', command=cambiar_color)
boton.pack()'''

def cambiar_color():
    if variable_control.get() == 1:
        ventana.config(bg='blue')
    elif variable_control.get() == 2:
        ventana.config(bg='red')

#Creacion de Radio Button
opcion1 = tk.Radiobutton(ventana, text="Azul",font=("Arial", 14), fg="blue",
                         variable=variable_control, value=1, command=cambiar_color)
#variable dice donde es que se va guardar el valor del radio button y value es el valor que
#identifica al radio button
opcion2 = tk.Radiobutton(ventana, text="Rojo",font=("Arial", 14), fg="blue",
                         variable=variable_control, value=2, command=cambiar_color)
opcion1.pack()
opcion2.pack()

ventana.mainloop()

#Como mantener el boton en forma sin importar el tamano de la letra
#Como hacer que el backgroudn no se ajuste al tamno de la letra
