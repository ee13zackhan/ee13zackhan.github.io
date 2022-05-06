# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:50:47 2022

@author: ee13zk
"""
import random
random.seed(1)
import numpy as np


data = []
data1 = []
multi = []

nrows = 3
ncols = 3
for i in range(0, nrows):
    row = []
    for j in range(0, ncols):
        row.append(random.randint(0,100))
    data.append(row)
    # print(row)
    
print(data)

for i in range(0, nrows):
    row = []
    for j in range(0, ncols):
        row.append(random.randint(0,100))
    data1.append(row)
    # print(row)
    
print(data1)

data2 = data1 * 2

print(data2)