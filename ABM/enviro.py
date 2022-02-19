# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: ee13zk
"""
import csv


environment = []

def make_enviro(file_path):
    f = open(file_path, newline='')
    reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)
    
    for row in reader:
        environment.append(row)
        
    f.close()
    
    return environment
