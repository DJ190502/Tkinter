import tkinter as tk

ventana = tk.Tk()

canvas = tk.Canvas(ventana, width=500, height=300, bg='lightblue')
canvas.pack(fill="both", expand=True)

canvas.create_text(150,50, text='Aprendiendo Canvas', fill='darkgreen',
                   font=("Courier", 12, 'italic'), justify='center')
canvas.pack()

ventana.mainloop()