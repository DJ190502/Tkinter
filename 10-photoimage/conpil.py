import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
etiqueta = tk.Label(ventana)

image_pil = Image.open("../static/image/wedding-4780256_1280.jpg")
imagen_redimensionada = image_pil.resize((50,50))
imagen_rotada = imagen_redimensionada.rotate(45)
image_tk = ImageTk.PhotoImage(imagen_rotada)

boton = tk.Button(ventana, image=image_tk)
boton.pack()

ventana.mainloop()

