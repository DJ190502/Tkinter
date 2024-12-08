import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo CheckButton")

'''def on_checkbutton_cambio():
    print("Checkbutton cambiado")
variable_check1=tk.BooleanVar()
check1 = tk.Checkbutton(ventana, text='Opcion 1',font=("Arial", 14), fg="blue", variable=variable_check1, command=on_checkbutton_cambio)
check1.pack()'''

def on_check_cambio():#Mediante el check activa y desactiva el estado de un boton
    if variable_check1.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

def on_press():
    print("Presionado")

variable_check1 = tk.BooleanVar()

check1 = tk.Checkbutton(ventana, text="Habilitar Boton", variable=variable_check1, command=on_check_cambio)
boton=tk.Button(ventana, text='Boton', state="disabled", command=on_press)#State es para el estado del boton
check1.pack()
boton.pack()

ventana.mainloop()


