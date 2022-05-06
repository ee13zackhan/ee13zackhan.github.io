# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:48:54 2022

@author: 200779106
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

# Create variables to hold the rasterdata from each file
geology = []
transport = []
population = []

# Create a function to read files

def make_raster(file_path, array):
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
        array.append(row)
        
    f.close()
    
    return array

# make_raster("best_geology.txt", geology)
# make_raster("best_transport.txt", transport)
make_raster("best_population.txt", population)

plt.imshow(population)