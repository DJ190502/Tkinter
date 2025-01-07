import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo de Listbox")

listbox = tk.Listbox(ventana, width=30, height=10, font=("Arial", 12), fg="white", bg="black")

listbox.insert(tk.END, 'Elemento 1')
listbox.insert(tk.END, 'Elemento 2')
listbox.insert(tk.END, 'Elemento 3')
listbox.insert(0,"Elemento 4")
listbox.insert(2,"Elemento 5")

listbox.delete(2)
listbox.delete(0)

def on_seleccionar(event):
    indice = listbox.curselection()
    elemento =  listbox.get(indice)
    print(f"Seleccionado: {elemento}")

listbox.bind("<<ListboxSelect>>", on_seleccionar)

listbox.pack()

ventana.mainloop()
