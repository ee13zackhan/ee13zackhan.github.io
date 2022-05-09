# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:44:35 2022

@author: ee13zk
"""

import unittest
import SiteLocator
import numpy as np

class TestSiteLocator(unittest.TestCase):
    
    def test_splitter(self):
        test = np.genfromtxt("test1.txt", delimiter=",")
        result = np.genfromtxt("result1.txt", delimiter=",")
        p = 50
        SiteLocator.splitter(test, p)
        self.assertEqual(test, result)
        
        test2 = np.genfromtxt("test2.txt", delimiter=",")
        result2 = np.genfromtxt("result2.txt", delimiter=",")
        p = 90
        SiteLocator.splitter(test2, p)
        self.assertEqual(test2, result2)
        
    # def test_smpl(self):
    #     test1 = np.genfromtxt("test1.txt", delimiter=",")
    #     test2 = np.genfromtxt("test2.txt", delimiter=",")
    #     test3 = np.genfromtxt("test3.txt", delimiter=",")
    #     var1 = 1
    #     var2 = 1
    #     var3 = 0
        
    
    # Talk about how i will implment testing with more time
        