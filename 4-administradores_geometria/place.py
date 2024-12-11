import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Place")

'''
#Coordenadas fijas
label1 = tk.Label(ventana, text="Label 1")
label1.place(x=50,y=50)

label2 = tk.Label(ventana, text="Label 2")
label2.place(x=100,y=100)

'''

#Coordenas relativas(porcentaje) es relativo al tamaño de la geometria por ejemplo el
# 50 % de una ventana de 300x300 seria 150 el objeto se veria en el 150 px
label1 = tk.Label(ventana, text="Label 1")
label1.place(relx=0.25,rely=0.25)

label2 = tk.Label(ventana, text="Label 2")
label2.place(relx=0.5,rely=0.5)


ventana.mainloop()