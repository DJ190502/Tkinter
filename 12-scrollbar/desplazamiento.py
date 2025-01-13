import tkinter as tk

ventana = tk.Tk()

scrollbar_vertical = tk.Scrollbar(ventana)
scrollbar_vertical.pack(side="right", fill='y')

ventana.mainloop()