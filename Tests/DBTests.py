'''
Created on 03.12.2018

@author: bernhard
'''
import unittest
from sodatamining.DBConnection import *

class DBTests(unittest.TestCase):
    
    def setUp(self):
        self.dbc = DBConnection()
    
    
    
        
    """Tests of the connections for sentiment"""
    def testGetBlockValue(self):
        output = self.dbc.get_postblock_value(159)
        correct = (81183011, 159, 158, 36.09, 17.8333, 0.051, 0.803, 0.146, 0.9715)
        
        self.failUnlessEqual(output, correct)
    
    def testGetHistoryValue(self):
        output = self.dbc.get_posthistory_value(254878)
        correct = (None, 254878, 254876,78.245, 8, 0.000 , 0.709, 0.291 , 0.7319)
        
        self.failUnlessEqual(output, correct)
        
    def testGetPredHistoryValue(self):
        output = self.dbc.get_predposthistory_value(254878)
        correct = (None, None, 254878, 78.245, 8, 0.000 , 0.709, 0.291 , 0.7319)
        
        self.failUnlessEqual(output, correct)
    
    
    
    