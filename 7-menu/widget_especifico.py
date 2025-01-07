import tkinter as tk

ventana = tk.Tk()

def mostrar_menu_contextual(event):
    menu_contextual.tk_popup(event.x_root, event.y_root)

menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Cortar")
menu_contextual.add_command(label="Copiar")
menu_contextual.add_command(label="Pegar")

entrada = tk.Entry(ventana)
entrada.pack()

entrada.bind("<Button-3>", mostrar_menu_contextual)

ventana.mainloop()