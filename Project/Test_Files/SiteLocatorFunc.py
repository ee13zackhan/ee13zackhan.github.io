# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:48:54 2022

@author: 200779106
"""

# Set Matplotlib to use Tkinter backend and other imports
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# geology_ar = np.genfromtxt("best_geology.txt", delimiter=",")
# population_ar = np.genfromtxt("best_population.txt", delimiter=",")
# transport_ar = np.genfromtxt("best_transport.txt", delimiter=",")

global output_ar
global output

# Set to False by default but changed to True when a figure has been created
output = False

def splitter(array, percent):
    """
    A function designed to find the nth percentile value of a NumPy array 
    and change the values below it to zero. The function does not change the 
    of the arraay.
    
    Note: The input array will be chnaged.

    Parameters
    ----------
    array : narray
        The NumPy array to be changed.
    percent : Int
        The percentile value to be calculated of the array.

    Returns
    -------
    pc : Int
        The percentile value of the array.

    """
    new = array.copy()
    
    pc = np.percentile(new[new>0], percent)
    # print(pc)
    
    new[new<pc] = np.nan
    
    return pc, new



def smpl(geology, population, transport, geo_slider, pop_slider, tra_slider, ten):
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
    geo_mult = geology * geo_slider
    pop_mult = population * pop_slider
    tra_mult = transport * tra_slider
    
    # Sum all the multiplied arrays
    added_df = geo_mult + pop_mult + tra_mult
    
    # Sum the slider values to get the number of arrays to be merged
    slider_sum = geo_slider + pop_slider + tra_slider
    # print(slider_sum)
    
    # Find the average
    output_ar = added_df/slider_sum
    
    # total_np = pd.DataFrame(total_df).to_numpy()
    
    top_ten = ten
    
    output = True
    
    # Close the previous figure window
    if output == True:
        matplotlib.pyplot.close()
    
    # Display the whole raster
    if not top_ten:
        plt.imshow(output_ar, cmap="Greys")
        return output_ar
    
    # Diplays the top 10 percent of the raster in blue
    else:
        pc, new = splitter(output_ar, 90)
        plt.imshow(output_ar, cmap="Greys")
        plt.imshow(new, cmap="Blues", vmin=pc-1)
        plt.show()
        return new


def adv(geology, population, transport, geo_slider, pop_slider, tra_slider, ten):
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
    geo_mult = geology * (geo_slider/100)
    pop_mult = population * (pop_slider/100)
    tra_mult = transport * (tra_slider/100)
    
    # Find the average by summing the multilied rasters
    output_ar = geo_mult + pop_mult + tra_mult
    
    slider_sum = geo_slider + pop_slider + tra_slider
    
    # If slider_sum exceeds 100%
    if slider_sum != 100:
        print("Error!", "The sum of the sliders MUST equal 100")
    
    # If slider_sum is ok
    else:
        top_ten = ten
        
        output = True
        
        # Close the previous figure window
        if output == True:
            matplotlib.pyplot.close()
        
        # Display the whole raster
        if not top_ten:
            plt.imshow(output_ar, cmap="Greys")
            return output_ar
        # Diplays the top 10 percent of the raster in blue
        else:
            pc, new = splitter(output_ar, 90)
            plt.imshow(output_ar, cmap="Greys")
            plt.imshow(new, cmap="Blues", vmin=pc-1)
            plt.show()
            return new


