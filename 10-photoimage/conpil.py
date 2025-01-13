import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
etiqueta = tk.Label(ventana)

image_pil = Image.open("../static/image/wedding-4780256_1280.jpg")
imagen_redimensionada = image_pil.resize((50,50))
image_tk = ImageTk.PhotoImage(imagen_redimensionada)

boton = tk.Button(ventana, image=image_tk)
boton.pack()

ventana.mainloop()

