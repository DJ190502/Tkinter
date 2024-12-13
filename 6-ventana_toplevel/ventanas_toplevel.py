from tkinter import *
import tkinter as tk

ventana = Tk()
ventana.title("Ventana Principal")
ventana.geometry("600x400")

ventana_toplevel =Toplevel(ventana)# Se crea una ventana aparte
ventana_toplevel.title("Ventana Toplevel")
ventana_toplevel.geometry("300x200+50+50")

ventana.mainloop()
