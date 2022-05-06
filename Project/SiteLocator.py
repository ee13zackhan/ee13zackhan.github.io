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
population = []

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

make_raster("best_geology.txt", geology)
make_raster("best_transport.txt", transport)
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

plt.imshow(geo_mult)
plt.imshow(tra_mult)
plt.imshow(pop_mult)

final = add_3_rasters(geo_mult, tra_mult, pop_mult)

plt.imshow(final)

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









