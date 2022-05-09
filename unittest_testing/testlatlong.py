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
        # Test for unset
        self.assertRaises(latlong.NotSetError, a.get_long)
        #Test for set
        a.set_long("10E")
        self.assertEqual(a.get_long(), "10E")
        # Test for badly set resetting default
        # Note as set_long throws an exception on bad arguments
        # we need to try-except this.
        try:
            a.set_long("blah")
        except:
            self.assertRaises(latlong.NotSetError, a.get_long)
        
        
        
        
    def test_get_long_degrees(self): 
        a = latlong.LatLong()
        self.assertRaises(latlong.NotSetError, a.get_long_degrees)
        a.set_long("10E")
        self.assertEqual(a.get_long_degrees(), 10)
        try:
            a.set_long("blah")
        except:
            self.assertRaises(latlong.NotSetError, a.get_long_degrees)
        
        
        
        
    def test_get_long_direction(self): 
        a = latlong.LatLong()
        self.assertRaises(latlong.NotSetError, a.get_long_direction)    
        a.set_long("10E")
        self.assertEqual(a.get_long_direction(), 10)
        try:
            a.set_long("blah")
        except:
            self.assertRaises(latlong.NotSetError, a.get_long_direction)
        
        
        
if __name__ == '__main__':
    unittest.main()