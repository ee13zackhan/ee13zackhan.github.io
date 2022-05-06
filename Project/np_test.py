# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
import matplotlib.pyplot as pt
import numpy as np
test = []

## Making raster test

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
#         array.append(row)
        
#     f.close()


# make_raster("test.txt", test)

# pt.imshow(test)

## Using NumPy test

# array1 = np.array([1,1,1,1],[2,2,2,2])
# array2 = np.array([1,1,1,1])
# array3 = np.append(array1, array2)
# print(array3)

## Adding arrays without NumPy test

# array1 = [[1,3,1,0],[1,2,3,4],[1,1,1]]
# array2 = [[1,1,6,1],[4,3,2,1],[1,1,1]]
# array3 = []
# for row in range(len(array1)):
#     temp = []
#     for i in range(len(array1[row])):
#         val = array1[row][i] + array2[row][i]
#         # print(val)
#         temp.append(val)
#         # print(temp)
#     array3.append(temp)
# print(array3)

# array4 = np.array([1,2])
# array5 = [3,4]
# array6 = np.append(array4, array5)


## multiplying arrays with a multiplier test

array7 = [[1,3,1,0],[1,2,3,4],[1,1,1,1]]
mult = 2
array8 = []
for row in range(len(array7)):
    temp = []
    for i in range(len(array7[row])):
        val = array7[row][i] * mult
        # print(val)
        temp.append(val)
        # print(temp)
    array8.append(temp)
print(array8)