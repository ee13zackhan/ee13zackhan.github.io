# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: 200779106
"""
import csv

# Make a list to hold the environment data
rstr = []


def make_enviro(file_path):
    """
    Function which returns a list containing the environment raster data

    Parameters
    ----------
    file_path : .csv file
        A comma seperated value file containing environment data for the agents 
        to interact with e.g. food for agents to eat 

    Returns
    -------
    rstr : list
        A 2D list containing the environment raster data
    """
    f = open(file_path, newline='')
    reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    
    for row in reader:
        rstr.append(row)
        
    f.close()
    
    return rstr
