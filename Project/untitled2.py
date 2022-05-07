# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:50:47 2022

@author: ee13zk
"""

import matplotlib.pyplot as plt
from tkinter import Frame, Button, Scale
import tkinter as tk
from tkinter import ttk
import pandas as pd

# # fig = pt.figure(figsize=(8,8))
# # ax = fig.add_axes([0, 0, 1, 1])

# root = tk.Tk()
# root.title("Site Locator")
# root.geometry("500x500")

# my_notebook = ttk.Notebook(root)
# my_notebook.pack()


# simple = Frame(my_notebook, width=500, height=500)
# advanced = Frame(my_notebook, width=500, height=500)

# simple.pack(fill="both", expand=1)
# advanced.pack(fill="both", expand=1)

# my_notebook.add(simple, text="Simple")
# my_notebook.add(advanced, text="Advanced")


# # root.wm_title("Site Locator")
# # canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master=root)
# # canvas._tkcanvas.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=1)

# slider1 = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal").pack()
# slider2 = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal").pack()
# slider3 = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal").pack()


# btn1 = Button(simple, text="Run").pack()

# slider4 = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal").pack()
# slider5 = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal").pack()
# slider6 = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal").pack()

# btn2 = Button(advanced, text="Run").pack()

# # menu_bar = tkinter.Menu(root)
# # root.config(menu=menu_bar)
# # model_menu = tkinter.Menu(menu_bar)
# # menu_bar.add_cascade(label="Model", menu=model_menu)
# # model_menu.add_command(label="Run Model")

# tk.mainloop()


def multiplier(raster, multiplier):
   
    multiplied = []
   
    for row in range(len(raster)):
        temp = []
        for i in range(len(raster[row])):
            val = raster[row][i] * multiplier
            # print(val)
            temp.append(val)
            # print(temp)
        multiplied.append(temp)
       
    return multiplied

def make_enviro(file_path):
    """
    A function which returns a list containing the environment raster data

    Parameters:
        
        file_path : .csv file
            A comma seperated value file containing environment data for the agents 
            to interact with e.g. food for agents to eat 

    Returns:
        
        rstr : list
            A 2D list containing the environment raster data
    # """
    # f = open(file_path, newline='')
    # reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    
    # for row in reader:
    #     rstr = Series(row)
        
        
    # f.close()
    df = pd.read_csv(file_path, header=None )
    # return df.describe()
    
    return df

def smpl():
    
    geo_mult = multiplier(rstr, 0.5)

rstr = make_enviro("test.txt")

# GUI
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

# Simple Tab

simple_fig = plt.Figure(figsize=(6,5), dpi=100)

geo_lbl_simp = tk.Label(simple, text="Geology")
pop_lbl_simp = tk.Label(simple, text="Population")
tra_lbl_simp = tk.Label(simple, text="Transport")

geo_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
pop_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
tra_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")

btn1 = Button(simple, text="Run", command=smpl)


geo_lbl_simp.grid(column=0, row=0)
pop_lbl_simp.grid(column=0, row=1)
tra_lbl_simp.grid(column=0, row=2)

geo_slider_simp.grid(column=1, row=0)
pop_slider_simp.grid(column=1, row=1)
tra_slider_simp.grid(column=1, row=2)


btn1.grid(column=1, row=3)

canvas_simp = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(simple_fig, master=simple)
canvas_simp._tkcanvas.grid(columnspan=3, column=0, row=4)





# menu_bar = tkinter.Menu(root)
# root.config(menu=menu_bar)
# model_menu = tkinter.Menu(menu_bar)
# menu_bar.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Run Model")


tk.mainloop()


