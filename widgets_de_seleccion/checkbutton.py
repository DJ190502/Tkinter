import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo CheckButton")

def on_checkbutton_cambio():
    print("Checkbutton cambiado")


variable_check1=tk.BooleanVar()

check1 = tk.Checkbutton(ventana, text='Opcion 1',font=("Arial", 14), fg="blue", variable=variable_check1, command=on_checkbutton_cambio)


check1.pack()


ventana.mainloop()