# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:44:35 2022

@author: ee13zk
"""

import unittest
import SiteLocatorFunc
import numpy as np

class TestSiteLocator(unittest.TestCase):
    
    def test_splitter(self):
        test = np.genfromtxt("test1.txt", delimiter=",")
        result = np.genfromtxt("result1.txt", delimiter=",")
        p = 50
        pc, new = SiteLocatorFunc.splitter(test, p)
        np.testing.assert_array_equal(new, result)
        print("Tested splitter() with 50th Percentile")
        
        test2 = np.genfromtxt("test2.txt", delimiter=",")
        result2 = np.genfromtxt("result2.txt", delimiter=",")
        p = 90
        pc, new = SiteLocatorFunc.splitter(test2, p)
        np.testing.assert_array_equal(new, result2)
        print("Tested splitter() with 90th Percentile")
        
    def test_smpl(self):
        test1 = np.genfromtxt("test1.txt", delimiter=",")
        test2 = np.genfromtxt("test2.txt", delimiter=",")
        test3 = np.genfromtxt("test3.txt", delimiter=",")
        result = np.genfromtxt("result4.txt", delimiter=",")
        sld1 = 1
        sld2 = 1
        sld3 = 0
        ten = 0
        new = SiteLocatorFunc.smpl(test1,test2,test3,sld1,sld2,sld3,ten)
        
        np.testing.assert_array_equal(new, result)
        print("Tested smpl() with merging 2 arrays")
        
        test1 = np.genfromtxt("test1.txt", delimiter=",")
        test2 = np.genfromtxt("test3.txt", delimiter=",")
        test3 = np.genfromtxt("test4.txt", delimiter=",")
        result = np.genfromtxt("result5.txt", delimiter=",")
        sld1 = 1
        sld2 = 1
        sld3 = 1
        ten = 1
        new = SiteLocatorFunc.smpl(test1,test2,test3,sld1,sld2,sld3,ten)
        
        np.testing.assert_array_equal(new, result)
        print("Tested smpl() with merging 3 arrays and only the top 10 percent")
        
    def test_adv(self):
        test1 = np.genfromtxt("test1.txt", delimiter=",")
        test2 = np.genfromtxt("test2.txt", delimiter=",")
        test3 = np.genfromtxt("test3.txt", delimiter=",")
        result = np.genfromtxt("result6.txt", delimiter=",")
        sld1 = 50
        sld2 = 25
        sld3 = 25
        ten = 0
        new = SiteLocatorFunc.smpl(test1,test2,test3,sld1,sld2,sld3,ten)
        
        np.testing.assert_array_equal(new, result)
        print("Tested adv() with merging 3 arrays")

if __name__ == '__main__':
    unittest.main()
    # Talk about how i will implment testing with more time
        