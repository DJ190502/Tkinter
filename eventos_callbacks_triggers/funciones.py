import tkinter as tk

def on_click(event):
    print("Boton presionado")
ventana = tk.Tk()

button = tk.Button(ventana, text="Haz clic aqui")
button.pack()

button.bind("<Button-1>", on_click)#Solo se ejecutara la funcion cuando se toque con el click izquierdo en el boton
#Es el boton no fuera del boton
def on_key_press(event):# Evento cuando se presione una tecla
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if event.char in abecedario:
        print(f"{event.char} esta en el abecedario")
    else:
        print(f"{event.char} no esta en el abecedario")

ventana.bind("<KeyPress>", on_key_press)# Key Press es evento o trigger que te permite asociar cualquier tecla

"""def on_resize(event): # Para imprimir redimensionar ventana o el movimiento asi como cualquier otra cosa
    print(f"La ventana ha sido redimensionada a {event.width}x{event.height}")

ventana.bind("<Configure>", on_resize)"""

def on_mouse_move(event):#Imprimir movimiento del mouse u otra cosa
    print(f"Raton movido a {event.x},{event.y}")

ventana.bind("<Motion>",on_mouse_move)#Motion para eventos con el movimiento del mouse


ventana.mainloop()