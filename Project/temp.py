# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import csv
# import matplotlib.pyplot as pt
import numpy as np
# test = []

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


# make_raster("M:/MSc/Programming/Project/test.txt", test)

# pt.imshow(test)

# array1 = np.array([1,1,1,1],[2,2,2,2])
# array2 = np.array([1,1,1,1])
# array3 = np.append(array1, array2)
# print(array3)

array1 = [[1,3,1,0],[1,2,3,4]]
array2 = [[1,1,6,1],[4,3,2,1]]
array3 = []
temp = 0
for row in range(len(array1)):
    if temp != 0:
        array3.append(temp)
    temp = []
    for i in range(len(array1[row])):
        val = array1[row][i] + array2[row][i]
        # print(val)
        temp.append(val)
        # print(temp)
print(array3)

# the code only appends the sum of the first lists within array1 and array2
# it doesnt append the second (although im pretty sure it does calculate it)
# i think it doesnt go back into the first for loop after changing val so it
# doesnt get appended. figure out how to fix it or try and make numpy arrays work