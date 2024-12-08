import tkinter as tk

windows = tk.Tk()

windows.title("Aprendizaje Automático") #Titulo
windows.geometry("800x600+280+50") #Tamaño y posicion en la pantalla
windows.minsize(400,400)#Tamaño Minimo
windows.maxsize(1366,768)#Tamaño Maximo
windows.iconbitmap('./static/icons/aa.ico')# Icono (Busca uno mejor)
windows.configure(bg="gray")#Background
windows.attributes("-alpha", 1) # Opacidad


windows.mainloop() #Loop para que funcione