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

def one_click(event):
    print("Clic en el Listbox")

def double_click(event):
    print("Doble clic en el Listbox")

listbox.bind("<<ListboxSelect>>", on_seleccionar)#Algo tiene que ver el <<>>
listbox.bind("<Button-1>", one_click)
listbox.bind("<Double-Button-1>", double_click)

listbox.pack()

ventana.mainloop()
