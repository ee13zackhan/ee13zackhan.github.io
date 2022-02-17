# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:10:18 2022

@author: ee13zk
"""
import csv
import matplotlib

environment = []

f = open("in.txt", newline='')
reader = csv.reader(f,quoting=csv.QUOTE_NONNUMERIC)

for row in reader:
    environment.append(row)
    
f.close()

# matplotlib.pyplot.xlim(0, 300)
# matplotlib.pyplot.ylim(0, 300)
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()
