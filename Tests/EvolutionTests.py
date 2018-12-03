'''
Created on 03.12.2018

@author: bernhard
'''

import unittest
from sodatamining.PostEvolution import *
from pip._vendor.requests.api import post

class EvolutionTests(unittest.TestCase):
    
    def setUp(self):
        self.pEvo = PostEvolution()
        
        self.posthistory = ('null',
                #'id': 
                123123, 
                #'predposthistoryid': 
                123122, 
                #'flesch_reading_ease': 
                10, 
                #'gunning_fog_index': 
                60,
                #'pos': 
                0.018, 
                #'neu': 
                0.915, 
                #'neg': 
                0.067,
                #'compound': 
                -0.8097
            )
        
        self.predposthistory = (
                #'placeholder':
                'null',
                #'placeholder':
                'null',
                #'id': 
                123122,  
                #'flesch_reading_ease': 
                50, 
                #'gunning_fog_index': 
                20,
                #'pos': 
                0.086, 
                #'neu': 
                0.914, 
                #'neg': 
                0.000,
                #'compound': 
                0.4404
            )
        
        self.postblock = (
                #'posthistoryid': 
                111, 
                #'id': 
                111115, 
                #'predpostblockversionid': 
                1111115, 
                #'flesch_reading_ease': 
                50, 
                #'gunning_fog_index': 
                20,
                #'pos': 
                0.018, 
                #'neu': 
                0.915, 
                #'neg': 
                0.067,
                #'compound': 
                -0.809
            )
        
        self.predpostblock = (
                #'posthistoryid': 
                100, 
                #'id': 
                111115,
                #'predpostblockid':
                None,  
                #'flesch_reading_ease': 
                44, 
                #'gunning_fog_index': 
                12,
                #'pos': 
                0.086, 
                #'neu': 
                0.914, 
                #'neg': 
                0.000,
                #'compound': 
                0.4404
            )
        
    def testInsertBlockEvoEntry(self):
        block = self.postblock
        preBlock = self.predpostblock
        change_type = 'readability_flesch_improved'
        
        correctOutput = {
                'posthistoryid': block[0],
                'changetype': change_type,
                'postblockid': block[1],
                'predpostblockid': preBlock,
                'valuenew': block[3],
                'valueold': preBlock[3]
            }
        output = self.pEvo.insert_evolution_entry('postblockevolution', block, 
                                                  preBlock, 'readability_flesch_improved', 
                                                  block[3] , preBlock[3])
        
        self.failUnlessEqual(output, correctOutput)
        
    def testInsertHistoryEvoEntry(self):
        post = self.posthistory
        prePost = self.predposthistory
        change_type = 'readability_flesch_improved'
        
        correctOutput = {
                'posthistoryid': post[0],
                'changetype': change_type,
                'postblockid': post[1],
                'predpostblockid': prePost,
                'valuenew': post[3],
                'valueold': prePost[3]
            }
        output = self.pEvo.insert_evolution_entry('postblockevolution', post, 
                                                  prePost, 'readability_flesch_improved', 
                                                  post[3] , prePost[3])
        
        self.failUnlessEqual(output, correctOutput)

    def testBlockEvaluateEvolution(self):
        block = self.postblock
        preBlock = self.predpostblock
        
        output = self.pEvo.evaluate_evolution('postblockevolution', block, preBlock)
        correctOutput = "readability_flesch_improved-readability_fox_aggravate-sentiment_com_aggravate"
        
        self.failUnlessEqual(output, correctOutput)
        
    def testHistoryEvaluateEvolution(self):
        post = self.posthistory
        prePost = self.predposthistory
        
        output = self.pEvo.evaluate_evolution('postblockevolution', post, prePost)
        correctOutput = "readability_flesch_aggravate-readability_fox_aggravate-sentiment_com_aggravate"
        
        self.failUnlessEqual(output, correctOutput)
        
        