# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:48:54 2022

@author: 200779106
"""

# Set Matplotlib to use Tkinter backend and other imports
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

geology_ar = np.genfromtxt("best_geology.txt", delimiter=",")
population_ar = np.genfromtxt("best_population.txt", delimiter=",")
transport_ar = np.genfromtxt("best_transport.txt", delimiter=",")

# A function used to change values of zero within the array
# Not needed anymore

# def remover(array):
    
#     array[array<1] = -255

# remover(geology_ar)
# remover(population_ar)
# remover(transport_ar)

# Testing the input arrays
# plt.imshow(geology_ar)
# plt.imshow(population_ar)
# plt.imshow(transport_ar)

# Declaring global variales

global output_ar
global output

# Set to False by default but changed to True when a figure has been created
output = False

def splitter(array, percent):
    """
    A function designed to find the nth percentile value of a NumPy array 
    and change the values below it to NaN. The function does not change the 
    array, it returns a new array.

    Parameters
    ----------
    array : Array of float64
        The NumPy array to be changed.
    percent : Int
        The percentile value to be calculated of the array.

    Returns
    -------
    pc : Int
        The percentile value of the array.
    new : Array of float64
        A new array with the values below the pc value set to NaN.

    """
    new = array.copy()
    
    pc = np.percentile(new[new>0], percent)
    # print(pc)
    
    new[new<pc] = np.nan
    
    return pc, new


def smpl():
    """
    A function that will combine upto three arrays by taking their average.
    
    The function takes inputs from the GUI slide bars using the ".get()" method 
    from tkinter.
    
    Returns
    -------
    The function uses the imshow() method from matplotlib.pyplot to show the 
    combined raster image.

    """
    global output
    global output_ar
    
    # Multiply the arrays by their slider value of 0 or 1
    geo_mult = geology_ar * geo_slider_simp.get()
    pop_mult = population_ar * pop_slider_simp.get()
    tra_mult = transport_ar * tra_slider_simp.get()
    
    # Sum all the multiplied arrays
    added_ar = geo_mult + pop_mult + tra_mult
    
    # Sum the slider values to get the number of arrays to be merged
    slider_sum = geo_slider_simp.get() + pop_slider_simp.get() + tra_slider_simp.get()
    # print(slider_sum)
    
    # Find the average
    output_ar = added_ar/slider_sum
    
    # total_np = pd.DataFrame(total_df).to_numpy()
    
    top_ten = var_simp.get()
    
    output = True
    
    # Close the previous figure window
    if output == True:
        matplotlib.pyplot.close()
    
    # Display the whole raster
    if not top_ten:
        plt.imshow(output_ar, cmap="Greys")
    
    # Diplays the top 10 percent of the raster in blue
    else:
        pc, new = splitter(output_ar, 90)
        plt.imshow(output_ar, cmap="Greys")
        plt.imshow(new, cmap="Blues", vmin=pc-1)
        plt.show()


def adv():
    """
    A function that will combine upto three arrays by weighting them according 
    to the slide bars in the GUI.
    
    The function takes inputs from the GUI slide bars using the ".get()" method 
    from tkinter.
    
    Returns
    -------
    The function uses the imshow() method from matplotlib.pyplot to show the 
    combined raster image.

    """
    
    global output
    global output_ar
    
    # Multiplies the raster by a multiplier (derived from the GUI input)
    geo_mult = geology_ar * (geo_slider_adv.get()/100)
    pop_mult = population_ar * (pop_slider_adv.get()/100)
    tra_mult = transport_ar * (tra_slider_adv.get()/100)
    
    # Find the average by summing the multilied rasters
    output_ar = geo_mult + pop_mult + tra_mult
    
    slider_sum = geo_slider_adv.get() + pop_slider_adv.get() + tra_slider_adv.get()
    
    # If slider_sum exceeds 100%
    if slider_sum != 100:
        messagebox.showerror("Error!", "The sum of the sliders MUST equal 100")
    
    # If slider_sum is ok
    else:
        top_ten = var_adv.get()
        
        output = True
        
        # Close the previous figure window
        if output == True:
            matplotlib.pyplot.close()
        
        # Display the whole raster
        if not top_ten:
            plt.imshow(output_ar, cmap="Greys")
        
        # Diplays the top 10 percent of the raster in blue
        else:
            pc, new = splitter(output_ar, 90)
            plt.imshow(output_ar, cmap="Greys")
            plt.imshow(new, cmap="Blues", vmin=pc-1)
            plt.show()


def save_output():
    """
    A function which allows the user to save the last figure displayed. Can be 
    saved as a CSV file in .txt format.

    Returns
    -------
    CSV file of the last figure displayed.

    """
    global output
    global output_ar
    
    # Displays an error message if no figure has been created
    if not output:
        messagebox.showerror("Error!", "There is no output\nUse the sliders and press the run button to create one first")
    # Opens a file dialogue window
    else:
        file = filedialog.asksaveasfilename(defaultextension=".txt", title="Save File", filetypes=(("Text Files", "*.txt"), ("CSV", "*.csv")))
        # If a file name is input, saves the file to that name
        if file:
            # Save the output as a file
            np.savetxt(file, output_ar, fmt="%d", delimiter=",")

# GUI Setup
root = tk.Tk()
root.title("Site Locator")
root.geometry("500x500")

notebook = ttk.Notebook(root)
notebook.pack()

# Create the two tabs, simple and advanced
simple = Frame(notebook, width=500, height=500)
advanced = Frame(notebook, width=500, height=500)

simple.pack(fill="both", expand=1)
advanced.pack(fill="both", expand=1)

notebook.add(simple, text="Simple")
notebook.add(advanced, text="Advanced")


# SIMPLE TAB

# Creates the labels for the sliders
geo_lbl_simp = tk.Label(simple, text="Geology")
pop_lbl_simp = tk.Label(simple, text="Population")
tra_lbl_simp = tk.Label(simple, text="Transport")

# Creates the sliders
geo_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
pop_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")
tra_slider_simp = Scale(simple, from_=0, to=1, resolution=1, length=50, orient="horizontal")

# Creates the check box and the variable to hold its value
var_simp = IntVar()
ten_check_simp = Checkbutton(simple, text="Top 10%", variable=var_simp)

# Creates the run and save buttons
run_btn_simp = Button(simple, text="Run", command=smpl)
sve_btn_simp = Button(simple, text="Save Output", command=save_output)

# This code was part of the code used to try open the figure in the ame window as the GUI
# but did not function as intended
# canvas_simp = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(simple_fig, master=simple)

# Layout all of the widgets created above
geo_lbl_simp.grid(column=0, row=0)
pop_lbl_simp.grid(column=0, row=1)
tra_lbl_simp.grid(column=0, row=2)


geo_slider_simp.grid(column=1, row=0)
pop_slider_simp.grid(column=1, row=1)
tra_slider_simp.grid(column=1, row=2)


ten_check_simp.grid(column=1, row=3)

run_btn_simp.grid(column=1, row=4)
sve_btn_simp.grid(column=1, row=5)


# ADVANCED TAB

# Creates the labels for the sliders
geo_lbl_adv = tk.Label(advanced, text="Geology")
pop_lbl_adv = tk.Label(advanced, text="Population")
tra_lbl_adv = tk.Label(advanced, text="Transport")

# Creates the sliders
geo_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
pop_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")
tra_slider_adv = Scale(advanced, from_=0, to=100, resolution=1, length=300, orient="horizontal")

# Creates the check box and the variable to hold its value
var_adv = IntVar()
ten_check_adv = Checkbutton(advanced, text="Top 10%", variable=var_adv)

# Creates the run and save buttons
run_btn_adv = Button(advanced, text="Run", command=adv)
sve_btn_adv = Button(advanced, text="Save Output", command=save_output)


# Layout all of the widgets created above
geo_lbl_adv.grid(column=0, row=0)
pop_lbl_adv.grid(column=0, row=1)
tra_lbl_adv.grid(column=0, row=2)

geo_slider_adv.grid(column=1, row=0)
pop_slider_adv.grid(column=1, row=1)
tra_slider_adv.grid(column=1, row=2)

ten_check_adv.grid(column=1, row=3)

run_btn_adv.grid(column=1, row=4)
sve_btn_adv.grid(column=1, row=5)

# Used to run the GUI
tk.mainloop()
