# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:27:38 2022

@author: ee13zk
"""


import unittest
import latlong

class TestLatLong(unittest.TestCase):


    def test_set_long(self):
        a = latlong.LatLong()
        a.set_long("10E")
        self.assertEqual(a.get_long(), "10E")
        self.assertRaises(latlong.NumberOutOfRangeError, a.set_long, "1000E") 
        self.assertRaises(latlong.NumberOutOfRangeError, a.set_long, "-1E")
        self.assertRaises(latlong.DirectionScrewyError, a.set_long, "10R")
        self.assertRaises(latlong.DirectionScrewyError, a.set_long, "10EE")
        
        
        
        
    def test_get_long(self):
        a = latlong.LatLong()
        # Ideally needs to check here that the value is set (see below).
        a.set_long("10E")
        self.assertEqual(a.get_long(), "10E")

        
        
        
    # Write this
    # Test for an exception if long_degrees == -1
    def test_get_long_degrees(self):
        a = latlong.LatLong()
        self.assertRaises(latlong.NumberOutOfRangeError, a.set_long_degrees, "-1")
        
        
        
        
    # Write this
    # Test for an exception if long_direction == ""
    def test_get_long_direction(self): 
        a = latlong.LatLong()
        self.assertRaises(latlong.NoDirectionError, a.set_long_direction, "")
        
        
        
if __name__ == '__main__':
    unittest.main()