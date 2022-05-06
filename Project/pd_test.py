# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:21:12 2022

@author: 200779106
"""
import csv
from pandas import Series, DataFrame
import pandas as pd
import random
random.seed(1)


# rstr = [4, 7, -5, 3]

# obj = Series(rstr, index=["a","b","c","d"])
# print(obj["d"])

rstr = []


def make_enviro(file_path):
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
        rstr = Series(row)
        
        
    f.close()
    
    return rstr