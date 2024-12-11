import tkinter as tk

ventana = tk.Tk()

texto = tk.StringVar(value="Hola, mundo!")
texto.set("CS") #El set cambia el valor anterior
print(texto.get()) #get es necesario para acceder a las variables

entrada = tk.Entry(ventana, textvariable=texto)
entrada.pack()

etiqueta = tk.Label(ventana)
etiqueta.pack()

def actualizar_etiqueta(*args): #Esta funcion actualiza la etiqueta
    etiqueta.config(text=texto.get())

texto.trace('w', actualizar_etiqueta) #este trace tracea o monitorea los cambios de escritura(w)(pueden ser de lectura)
#que se manifiestan en texto

ventana.mainloop()