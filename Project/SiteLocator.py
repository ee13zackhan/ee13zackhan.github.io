# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:01:51 2022

@author: 200779106
"""
import csv
# Set Matplotlib to use TkInter backend
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from tkinter import Frame, Button, Scale
import tkinter as tk
from tkinter import ttk
import numpy as np
import pandas as pd

# import numpy as np

# Create variables to hold the rasterdata from each file
geology = np.array()
transport = np.array()
population = np.array()

# Create a function to read files

# def make_raster(file_path, array):
#     """
#     A function which returns a list containing the environment raster data

#     Parameters:
        
#         file_path: .csv file
#             A comma seperated value file containing environment data for the agents 
#             to interact with e.g. food for agents to eat
            
#         array: list
#             The array to which the raster data will be appended

#     Returns:
        
#         array: 2D list
#             The updated input array
#     """
#     f = open(file_path, newline='')
#     reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    
#     for row in reader:
#         np.append(array, row)
        
#     f.close()
    
#     return array

def make_raster(file_path, ar):
    """
    A function which returns a list containing the environment raster data

    Parameters:
        
        file_path : .csv file
            A comma seperated value file containing environment data for the agents 
            to interact with e.g. food for agents to eat 

    Returns:
        
        rstr : list
            A 2D list containing the environment raster data
    """
    f = open(file_path, newline='')
    reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    
    for row in reader:
        ar.append(row)
        
    f.close()
    
    return np.array(ar)

make_raster("best_geology.txt", geology)
make_raster("best_transport.txt", transport)
make_raster("best_population.txt", population)

print(geology)

# Check for geology
# if geology != []:
#     geo = True
# else:
#     geo = False

# # Check for transport
# if transport != []:
#     tra = True
# else:
#     tra = False
    
# # Check for population
# if population != []:
#     pop = True
# else:
#     pop = False

# Check they are being read properly

# plt.imshow(geology)
# plt.imshow(transport)
# plt.imshow(population)

# plt.imshow(population)
# plt.show()



## multiply a map with a multiplier

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

def add_3_rasters(raster1, raster2, raster3):
    added = []
    for row in range(len(raster1)):
        temp = []
        for i in range(len(raster1[row])):
            val = raster1[row][i] + raster2[row][i] + raster3[row][i]
            # print(val)
            temp.append(val)
            # print(temp)
        added.append(temp)
    return added

def spl(raster1, raster2, raster3):
    
    # geo_bool = bool(slider1.get())
    # # print(geo_bool)
    # pop_bool = bool(slider2.get())
    # # print(pop_bool)
    # tra_bool = bool(slider3.get())
    # # print(tra_bool)
    
    geo = multiplier(geology, slider1.get())
    pop = multiplier(population, slider2.get())
    tra = multiplier(transport, slider3.get())
    
    slider_sum = slider1.get() + slider2.get() + slider3.get()
    # print(slider_sum)
    
    added = add_3_rasters(geo, pop, tra)
        
    output_raster = multiplier(added, 1/slider_sum)
    
    return output_raster
    
# def adv():
    
#     geo_multiplier = slider1.get()/100
#     pop_multiplier = slider2.get()/100
#     tra_multiplier = slider3.get()/100
    

# mult = 2
# pop_mult = []
# for row in range(len(population)):
#     temp = []
#     for i in range(len(population[row])):
#         val = population[row][i] * mult
#         # print(val)
#         temp.append(val)
#         # print(temp)
#     pop_mult.append(temp)


# geo_mult = []
# for row in range(len(geology)):
#     temp = []
#     for i in range(len(geology[row])):
#         val = geology[row][i] * mult
#         # print(val)
#         temp.append(val)
#         # print(temp)
#     geo_mult.append(temp)


geo_mult = multiplier(geology, 0.33)
tra_mult = multiplier(transport, 0.33)
pop_mult = multiplier(population, 0.33)

# plt.imshow(geo_mult)
# plt.imshow(tra_mult)
# plt.imshow(pop_mult)

final = add_3_rasters(geo_mult, tra_mult, pop_mult)

# plt.imshow(final)

# Adding arrays

# combined = []
# for row in range(len(pop_mult)):
#     temp = []
#     for i in range(len(pop_mult[row])):
#         val = pop_mult[row][i] + geo_mult[row][i]
#         # print(val)
#         temp.append(val)
#         # print(temp)
#     combined.append(temp)

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







