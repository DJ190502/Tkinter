import tkinter as tk

def copiar():
    texto.event_generate("<<Copy>>")

def cortar():
    texto.event_generate("<<Cut>>")

def pegar():
    texto.event_generate("<<Paste>>")

ventana = tk.Tk()
texto = tk.Text(ventana)
texto.pack()

boton_copiar = tk.Button(ventana, text="Copiar", command=copiar)
boton_copiar.pack()

boton_cortar = tk.Button(ventana, text="Cortar", command=cortar)
boton_cortar.pack()

boton_pegar = tk.Button(ventana, text="Pegar", command=pegar)
boton_pegar.pack()

ventana.mainloop()
