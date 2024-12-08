import tkinter as tk

ventana = tk.Tk()

ventana.title("Frames")

label = tk.Label(ventana, text="Ingrese Archivo")#Etiqueta
label.config(text="Es lo nuevo", fg="blue", bg="yellow", font=("Sans-Serif", 14, "bold"))#Cambie el texto y los atributos
label.pack()#Empacado

ventana.mainloop()