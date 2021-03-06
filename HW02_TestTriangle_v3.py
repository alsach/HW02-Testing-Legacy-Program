# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:58:11 2021

@author: UserA
"""

import unittest

from HW02_Triangle_v2 import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangle(self): 
        self.assertTrue(classifyTriangle(3,4,5),'Right')

    def testscaleneTriangle(self): 
        self.assertTrue(classifyTriangle(10,13,8),'Scalene')
        
    def testEquilateralTriangles(self): 
        self.assertTrue(classifyTriangle(1,1,1),'Equilateral')
        
    def testIsoscelesTriangles(self):
        self.assertTrue(classifyTriangle(3,3,5), 'Isosceles')
        
    def testBigNumbers(self):
        self.assertTrue(classifyTriangle(201, 4, 5), 'InvalidInput')
        
    def testSmallNumber(self):
        self.assertTrue(classifyTriangle(-1, 4, 5), 'InvalidInput')
        
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()