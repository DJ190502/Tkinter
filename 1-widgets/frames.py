import tkinter as tk

ventana = tk.Tk()

ventana.title("Frames")
ventana.geometry("800x600")
ventana.configure(bg="gray")

labelframe = tk.LabelFrame(ventana, text="Grupo de Widgets", bg='white', padx=10, pady=10)#Frame con etiqueta
labelframe.configure(width=300,height=200)
labelframe.pack()


"""frame1 = tk.Frame(ventana)#Se inicializa el frame
frame1.configure(width=300, height=400, bg='blue', bd=5)#Tamaño, background, borde
frame1.pack()
frame2 = tk.Frame(frame1)#Frame dentro del frame
frame2.configure(width=150, height=200, bg='yellow', bd='10')
frame2.pack()
boton = tk.Button(frame1, text="Goal")
frame2.pack()
boton.pack()"""

ventana.mainloop()