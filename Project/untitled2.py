# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:50:47 2022

@author: ee13zk
"""

import matplotlib.pyplot as plt
# from tkinter import Frame, Button, Scale
# import tkinter as tk
# from tkinter import ttk
import pandas as pd
import numpy as np
import math

# rstr = pd.read_csv("test.txt", header=None )


# plt.imshow(rstr)

# for i in rstr.index:
#     count = 0
#     if i != 0:
#         count = count + 1

# To iterate over columns

# for key, value in rstr.iteritems():
#     for i in range(len(value)):
#         print(value[i])

# count = 0

# To iterate over rows

# for key, value in rstr.iterrows():
#     for i in range(len(value)):
#         val = value[i]
#         # print(val)
#         if val != 0:
#             count = count + 1

# # print(count)
# ten_pc = math.ceil(count/10)
# print(ten_pc)
        

# lrg = rstr.nlargest(n=2 , columns=[0,1,2,3], keep="all")
# lrg = rstr.max(axis=1).max()
# print(lrg)

# lrg1 = lrg.max(axis=1)
# print(lrg1)

# rstr_np = pd.DataFrame(rstr).to_numpy()

# # print(rstr_np)
# plt.imshow(rstr)

# def cutter(data, percent):
    
    
#     pc = np.percentile(data[data>0], percent)
#     print(pc)
#     data[data<pc] = 0

# plt.imshow(rstr_np)

# lrg = cutter(rstr_np, 90)
# print(lrg)

# plt.imshow(rstr_np)
geology_ar = np.genfromtxt("best_geology.txt", delimiter=",")
population_ar = np.genfromtxt("best_population.txt", delimiter=",")
transport_ar = np.genfromtxt("best_transport.txt", delimiter=",")

def remover(array):
    
    array[array<1] = 5

remover(geology_ar)

# geo_mult = geology_ar * 1
# pop_mult = population_ar * 1
# tra_mult = transport_ar * 1

# added_df = geo_mult + pop_mult + tra_mult

# slider_sum = 1 + 1 + 1
# # print(slider_sum)

# output_ar = added_df/slider_sum

# plt.imshow(output_ar)



