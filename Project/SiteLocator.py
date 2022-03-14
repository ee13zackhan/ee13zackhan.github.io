# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:01:51 2022

@author: 200779106
"""
import csv
import matplotlib.pyplot as pt

# Create variables to hold the rasterdata from each file
geology = []
transport = []
population = []

# Create a function to read files

def make_raster(file_path, array):
    """
    A function which returns a list containing the environment raster data

    Parameters:
        
        file_path: .csv file
            A comma seperated value file containing environment data for the agents 
            to interact with e.g. food for agents to eat
            
        array: list
            The array to which the raster data will be appended

    Returns:
        
        array: 2D list
            The updated input array
    """
    f = open(file_path, newline='')
    reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    
    for row in reader:
        array.append(row)
        
    f.close()
    
    return array

make_raster("best_geology.txt", geology)
make_raster("best_transport.txt", transport)
make_raster("best_population.txt", population)



# pt.imshow(geology)
pt.imshow(transport)
# pt.imshow(population)