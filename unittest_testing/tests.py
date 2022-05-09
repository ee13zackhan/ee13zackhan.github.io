# -*- coding: utf-8 -*-
"""
Created on Mon May  9 19:14:16 2022

@author: ee13zk
"""

# test.py
import unittest
import docs

class TestDocs(unittest.TestCase):

    def test_add(self):
        a = docs.Calc()
        self.assertEqual(a.add(1,2), 3)


if __name__ == '__main__':
    unittest.main()