import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
etiqueta = tk.Label(ventana)

image_pil = Image.open("../static/image/wedding-4780256_1280.jpg")

image_tk = ImageTk.PhotoImage(image_pil)

boton = tk.Button(ventana, image=image_tk)
boton.pack()

ventana.mainloop()

