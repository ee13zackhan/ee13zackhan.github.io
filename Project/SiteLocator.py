# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:48:54 2022

@author: 200779106
"""

# Set Matplotlib to use Tkinter backend
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
# import pandas as pd
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create dataframe to hold the rasterdata from each file
# Use Pandas to read the CSV file

# geology_df = pd.read_csv("best_geology.txt", header=None)
# population_df = pd.read_csv("best_population.txt", header=None)
# transport_df = pd.read_csv("best_transport.txt", header=None)

# Used Pandas, but realised it was easier to use NumPy as it has a
# percentile Function

geology_ar = np.genfromtxt("best_geology.txt", delimiter=",")
population_ar = np.genfromtxt("best_population.txt", delimiter=",")
transport_ar = np.genfromtxt("best_transport.txt", delimiter=",")

# def remover(array):
    
#     array[array<1] = -255

# remover(geology_ar)
# remover(population_ar)
# remover(transport_ar)

# plt.imshow(geology_ar)
# plt.imshow(population_ar)
# plt.imshow(transport_ar)
global output_ar
global output

output = False

def splitter(array, percent):
    """
    

    Parameters
    ----------
    array : TYPE
        DESCRIPTION.
    percent : TYPE
        DESCRIPTION.

    Returns
    -------
    pc : TYPE
        DESCRIPTION.

    """
    pc = np.percentile(array[array>0], percent)
    # print(pc)
    array[array<pc] = 0
    
    return pc

def smpl():
    global output
    global output_ar
    
    output = True

    matplotlib.pyplot.close()
    
    geo_mult = geology_ar * geo_slider_simp.get()
    pop_mult = population_ar * pop_slider_simp.get()
    tra_mult = transport_ar * tra_slider_simp.get()
    
    added_df = geo_mult + pop_mult + tra_mult
    
    slider_sum = geo_slider_simp.get() + pop_slider_simp.get() + tra_slider_simp.get()
    # print(slider_sum)
    
    output_ar = added_df/slider_sum
    
    # total_np = pd.DataFrame(total_df).to_numpy()
    
    top_ten = var_simp.get()
    
    if not top_ten:
        plt.imshow(output_ar, cmap="Greys")
    else:
        pc = splitter(output_ar, 90)
        plt.imshow(output_ar, cmap="Blues", vmin=pc-1)
    
    ###### Double check that the above function is working as intended

def adv():
    global output
    global output_ar
    
    output = True
    
    matplotlib.pyplot.close()
    
    geo_mult = geology_ar * (geo_slider_adv.get()/100)
    pop_mult = population_ar * (pop_slider_adv.get()/100)
    tra_mult = transport_ar * (tra_slider_adv.get()/100)
    
    output_ar = geo_mult + pop_mult + tra_mult
    
    top_ten = var_adv.get()
    
    if not top_ten:
        plt.imshow(output_ar, cmap="Greys")
    else:
        pc = splitter(output_ar, 90)
        plt.imshow(output_ar, cmap="Blues", vmin=pc-1)

    #####   Double check that the above function is working as intended

def save_output():
    global output
    global output_ar
    
    if not output:
        messagebox.showerror("Error!", "There is no output\nUse the sliders as run button to create one first")
    else:
        file = filedialog.asksaveasfilename(defaultextension=".txt", title="Save File", filetypes=(("Text Files", "*.txt"), ("CSV", "*.csv")))
        if file:
            # Save the file
            np.savetxt(file, output_ar, fmt="%d", delimiter=",")

# GUI
root = tk.Tk()
root.title("Site Locator")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack()

simple = Frame(notebook, width=500, height=500)
advanced = Frame(notebook, width=500, height=500)

simple.pack(fill="both", expand=1)
advanced.pack(fill="both", expand=1)

notebook.add(simple, text="Simple")
notebook.add(advanced, text="Advanced")

# root.wm_title("Site Locator")




# SIMPLE TAB

geo_lbl_simp = tk.Label(simple, text="Geology")
pop_lbl_simp = tk.Label(simple, text="Population")
tra_lbl_simp = tk.Label(simple, text="Transport")
# ten_lbl_simp = tk.Label(simple, text="Top 10% Only")

geo_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
pop_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
tra_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
# ten_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")

var_simp = IntVar()
ten_check_simp = Checkbutton(simple, text="Top 10%", variable=var_simp)

run_btn_simp = Button(simple, text="Run", command=smpl)
sve_btn_simp = Button(simple, text="Save Output", command=save_output)

# canvas_simp = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(simple_fig, master=simple)
# Comment above line

geo_lbl_simp.grid(column=0, row=0)
pop_lbl_simp.grid(column=0, row=1)
tra_lbl_simp.grid(column=0, row=2)
# ten_lbl_simp.grid(column=0, row=3)

geo_slider_simp.grid(column=1, row=0)
pop_slider_simp.grid(column=1, row=1)
tra_slider_simp.grid(column=1, row=2)
# ten_slider_simp.grid(column=1, row=3)

ten_check_simp.grid(column=1, row=3)

run_btn_simp.grid(column=1, row=4)
sve_btn_simp.grid(column=1, row=5)

# out.pack(side="bottom")

# canvas_simp._tkcanvas.grid(columnspan=3, column=0, row=4)
# Comment above line




# ADVANCED TAB

geo_lbl_adv = tk.Label(advanced, text="Geology")
pop_lbl_adv = tk.Label(advanced, text="Population")
tra_lbl_adv = tk.Label(advanced, text="Transport")
# ten_lbl_adv = tk.Label(advanced, text="Top 10% Only")

geo_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
pop_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
tra_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
# ten_slider_adv = Scale(advanced, from_=0, to=1, resolution=1, length=50, orient="horizontal")

var_adv = IntVar()
ten_check_adv = Checkbutton(advanced, text="Top 10%", variable=var_adv)

run_btn_adv = Button(advanced, text="Run", command=adv)
sve_btn_adv = Button(advanced, text="Save Output", command=save_output)

geo_lbl_adv.grid(column=0, row=0)
pop_lbl_adv.grid(column=0, row=1)
tra_lbl_adv.grid(column=0, row=2)
# ten_lbl_adv.grid(column=0, row=3)

geo_slider_adv.grid(column=1, row=0)
pop_slider_adv.grid(column=1, row=1)
tra_slider_adv.grid(column=1, row=2)
# ten_slider_adv.grid(column=1, row=3)

ten_check_adv.grid(column=1, row=3)

run_btn_adv.grid(column=1, row=4)
sve_btn_adv.grid(column=1, row=5)



# menu_bar = tkinter.Menu(root)
# root.config(menu=menu_bar)
# model_menu = tkinter.Menu(menu_bar)
# menu_bar.add_cascade(label="Model", menu=model_menu)
# model_menu.add_command(label="Run Model")


tk.mainloop()
