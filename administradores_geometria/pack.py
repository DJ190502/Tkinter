import tkinter as tk


ventana = tk.Tk()
ventana.title("Ejemplo practico de Pack")

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton1 = tk.Button(frame_botones, text= "Boton 1")
boton1.pack(side='left', padx=5) # Posiciona el boton (side) de acuerdo
# a la posicion left al izquieda del frame, right a la derecha del frame

boton2 = tk.Button(frame_botones, text= "Boton 2")
boton2.pack(side='left', padx=5)

boton3 = tk.Button(frame_botones, text= "Boton 3")
boton3.pack(side='left', padx=5)


ventana.mainloop()