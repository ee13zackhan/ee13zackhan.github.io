# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:50:47 2022

@author: ee13zk
"""

import matplotlib
matplotlib.use("TkAgg")
from tkinter import Frame, Button, Scale
import tkinter as tk
from tkinter import ttk


# fig = pt.figure(figsize=(8,8))
# ax = fig.add_axes([0, 0, 1, 1])

root = tk.Tk()
root.title("Site Locator")
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack()


simple = Frame(my_notebook, width=500, height=500)
advanced = Frame(my_notebook, width=500, height=500)

simple.pack(fill="both", expand=1)
advanced.pack(fill="both", expand=1)

my_notebook.add(simple, text="Simple")
my_notebook.add(advanced, text="Advanced")


# root.wm_title("Site Locator")
# canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master=root)
# canvas._tkcanvas.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=1)

slider1 = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal").pack()
slider2 = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal").pack()
slider3 = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal").pack()


btn1 = Button(simple, text="Run").pack()

slider4 = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal").pack()
slider5 = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal").pack()
slider6 = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal").pack()

btn2 = Button(advanced, text="Run").pack()

# menu_bar = tkinter.Menu(root)
# root.config(menu=menu_bar)
# model_menu = tkinter.Menu(menu_bar)
# menu_bar.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Run Model")


tk.mainloop()