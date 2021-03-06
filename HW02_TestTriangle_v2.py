# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 09:13:20 2021

@author: Alisha Sacharoff

"""


import unittest

from HW02_Triangle_v2 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertTrue(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertTrue(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertTrue(classifyTriangle(1,1,1),'Equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()