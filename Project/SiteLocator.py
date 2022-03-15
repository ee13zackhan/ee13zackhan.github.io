# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:01:51 2022

@author: 200779106
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

# Create variables to hold the rasterdata from each file
geology = []
transport = []
population = np.zeros(335)

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
        np.append(array, row)
        
    f.close()
    
    return array

# make_raster("best_geology.txt", geology)
# make_raster("best_transport.txt", transport)
make_raster("best_population.txt", population)

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

plt.imshow(population, interpolation= "none")
plt.show()

# Merge the maps together into one map

# merged = []
# for row in range(len(array1)):
#     temp = []
#     for i in range(len(array1[row])):
#         val = array1[row][i] + array2[row][i]
#         # print(val)
#         temp.append(val)
#         # print(temp)
#     merged.append(temp)
# print(merged)