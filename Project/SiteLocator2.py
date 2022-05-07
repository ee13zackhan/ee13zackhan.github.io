# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:48:54 2022

@author: 200779106
"""

# Set Matplotlib to use Tkinter backend
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tkinter import Frame, Button, Scale, Canvas
import tkinter as tk
from tkinter import ttk
# import numpy as np
import pandas as pd
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
    # print(slider_sum)
    
    output_df = added_df/slider_sum

    

    # canvas_simp.draw()
    # show_me(output_df)
    
    # mycanvas = Canvas(simple)
    # mycanvas.grid(column=1, row=5)
    
    # mycanvas.create_image(0,0, image=output_df)
    
    # plt.imshow(output_df)
    # return output_df
    
    
    ###### Double check that the above function is working as intended

def adv():
    geo_mult = geology_df * (geo_slider_adv.get()/100)
    pop_mult = population_df * (pop_slider_adv.get()/100)
    tra_mult = transport_df * (tra_slider_adv.get()/100)
    
    output_df = geo_mult + pop_mult + tra_mult
    
    # plt.imshow(output_df)
    # return output_df

    ######   Double check that the above function is working as intended

# def show_me(df):
#     return plt.imshow(df)
    

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

canvas_simp = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(simple_fig, master=simple)
# Commetn above line

geo_lbl_simp.grid(column=0, row=0)
pop_lbl_simp.grid(column=0, row=1)
tra_lbl_simp.grid(column=0, row=2)

geo_slider_simp.grid(column=1, row=0)
pop_slider_simp.grid(column=1, row=1)
tra_slider_simp.grid(column=1, row=2)


btn1.grid(column=1, row=3)

canvas_simp._tkcanvas.grid(columnspan=3, column=0, row=4)
# Comment above line

# Advanced Tab

geo_lbl_adv = tk.Label(advanced, text="Geology")
pop_lbl_adv = tk.Label(advanced, text="Population")
tra_lbl_adv = tk.Label(advanced, text="Transport")

geo_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
pop_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
tra_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")

btn2 = Button(advanced, text="Run", command=adv)

geo_lbl_adv.grid(column=0, row=0)
pop_lbl_adv.grid(column=0, row=1)
tra_lbl_adv.grid(column=0, row=2)

geo_slider_adv.grid(column=1, row=0)
pop_slider_adv.grid(column=1, row=1)
tra_slider_adv.grid(column=1, row=2)


btn2.grid(column=1, row=3)



# menu_bar = tkinter.Menu(root)
# root.config(menu=menu_bar)
# model_menu = tkinter.Menu(menu_bar)
# menu_bar.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Run Model")


tk.mainloop()
