import tkinter as tk

ventana= tk.Tk()
ventana.title("Ejemplo Label")

etiqueta = tk.Label(ventana, text="Entrada de palabras")
etiqueta.pack()

entrada = tk.Entry(ventana)#un input
entrada.configure(fg="white", bg="green", font=("Arial",12))
entrada.insert(0, 'Ingrese algo')# Texto por defecto
entrada.pack()

frame =tk.Frame(ventana)
frame.configure(width=700, height=400, bg="blue", bd=5,)
frame.pack_propagate(False)# No deja que el label redimensione el frame
frame.pack()



def aplicar_texto(event=None):
    texto = entrada.get()  # entrada.get() para coger el texto
    label = tk.Label(frame, text="")
    label.config(text=texto)
    label.pack()

"""
def aplicar_texto(event=None):
    global label  # Definimos la variable label como global para poder acceder a ella
    texto = entrada.get()  # Obtenemos el texto de la entrada

    # Si ya existe un label, lo eliminamos
    if 'label' in globals():
        label.pack_forget()  # O label.destroy() para eliminarlo completamente

    # Creamos un nuevo label con el texto ingresado
    label = tk.Label(frame, text=texto)
    label.pack()

"""



boton_aplicar = tk.Button(ventana, text="Enter", command=aplicar_texto)
# entrada.get() para coger el texto
boton_aplicar.pack()

ventana.bind("<Return>", aplicar_texto)

ventana.mainloop()



