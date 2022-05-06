# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:48:54 2022

@author: 200779106
"""

# Set Matplotlib to use Tkinter backend
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tkinter import Frame, Button, Scale
import tkinter as tk
from tkinter import ttk
# import numpy as np
import pandas as pd


# Create dataframe to hold the rasterdata from each file
# Use Pandas to read the CSV file

geology_df = pd.read_csv("best_geology.txt", header=None)
population_df = pd.read_csv("best_population.txt", header=None)
transport_df = pd.read_csv("best_transport.txt", header=None)

# plt.imshow(geology_df)
# plt.imshow(population_df)
# plt.imshow(transport_df)

def smpl():
    
    geo_mult = geology_df * geo_slider_simp.get()
    pop_mult = population_df * pop_slider_simp.get()
    tra_mult = transport_df * tra_slider_simp.get()
    
    added_df = geo_mult + pop_mult + tra_mult
    
    slider_sum = geo_slider_simp.get() + pop_slider_simp.get() + tra_slider_simp.get()
    print(slider_sum)
    
    output_df = added_df/slider_sum
    
    plt.imshow(output_df)
    # return output_df
    
    ###### Double check that the above function is working as intended

def adv():
    geo_mult = geology_df * (geo_slider_adv.get()/100)
    pop_mult = population_df * (pop_slider_adv.get()/100)
    tra_mult = transport_df * (tra_slider_adv.get()/100)
    
    output_df = geo_mult + pop_mult + tra_mult
    
    plt.imshow(output_df)
    # return output_df

    ######   Double check that the above function is working as intended

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
# canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master=root)
# canvas._tkcanvas.pack(side=tkinter.TOP,fill=tkinter.BOTH,expand=1)

geo_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
pop_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
tra_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")

geo_slider_simp.pack()
pop_slider_simp.pack()
tra_slider_simp.pack()

btn1 = Button(simple, text="Run", command=smpl).pack() # may have to split this into two like above if get error


geo_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
pop_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
tra_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")

geo_slider_adv.pack()
pop_slider_adv.pack()
tra_slider_adv.pack()

btn2 = Button(advanced, text="Run", command=adv).pack()



# menu_bar = tkinter.Menu(root)
# root.config(menu=menu_bar)
# model_menu = tkinter.Menu(menu_bar)
# menu_bar.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Run Model")


tk.mainloop()
