# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:12:55 2022

@author: ee13zk
"""

"""
Add two random numbers together

Requires no setup. 
"""
import random

numA = random.random() * 10
"""Random number 1"""
    
numB = random.random() * 10    
"""Random number 2"""    

class Calc():
    """Provide methods for a calculator

    add -- Add two numbers and return sum.
    """    
    
    def add (self, num1, num2):
        """Add two numbers and return sum.
    
        Postional arguments:
        num1 -- an integer or double number (no default)
        num2 -- an integer or double number (no default)
    
        Returns:
        Sum of the two numbers.
        """
        return num1 + num2    

calc = Calc()
print(calc.add(numA, numB))