'''
Created on 17.12.2018

@author: bernhard
'''

import matplotlib.pyplot as plt
import numpy as np
from DBConnection import *

class EvolutionAnalysis(object):
    
    flesch_reading_ease = 12
    gunning_fog_index = 13
    compound = 19
    

    def __init__(self):
        self.dbc = DBConnection()
        
        self.pId = 15942975
        self.closedpId = 8799764
        
        self.closedpId2 = 12470206
        self.closedpId3 = 50232844
        
        self.acceptedId = 17261284
        
        
        self.plot_graph_of(self.pId)
        self.plot_graph_of(self.closedpId, True, True)
        
        self.plot_graph_of(self.closedpId2, True)
        self.plot_graph_of(self.closedpId3, True)
        
        self.plot_graph_of(self.acceptedId, False, True)
    
    def plot_graph_of(self, pId, closed=False, accepted=False):
        preds = self.dbc.get_all_predecessors(pId)
        
        xAxis = len(preds)
        flesch = []
        fog = []
        comp = []
        
        for pred in preds:
            flesch.append(pred[self.flesch_reading_ease])
            fog.append(pred[self.gunning_fog_index])
            comp.append(pred[self.compound])
        
        #The post got closed at some point   
        if closed:
            closedPos = self.get_closed_position(preds, self.dbc.get_closed_date(pId)[0])
            
        #The post got accepted at some point
        if accepted: 
            acceptedPos = self.get_accepted_postition(preds, pId)
            print acceptedPos
                    
        plt.figure(1, figsize=(18,5))
        
        """draw flesch reading ease graph"""
        plt.subplot(131)
        plt.title('Flesch-Reading-Ease')
        flesch_ar = np.array(flesch)
        x = np.arange(1,xAxis+1, 1)
        plt.plot(x, flesch_ar)
        if accepted: plt.plot(acceptedPos, flesch_ar[acceptedPos-1], 'bs')
        if closed: plt.plot(closedPos, flesch_ar[closedPos-1], 'rX')
                    
        """draw gunning fog graph"""
        plt.subplot(132)
        plt.title('Gunning-Fog-Index')
        fog_ar = np.array(fog)
        x = np.arange(1,xAxis+1, 1)
        plt.plot(x, fog_ar)
        if accepted: 
            plt.plot(acceptedPos, fog_ar[acceptedPos-1], 'bs', label='accepted')
            plt.legend(loc=0, bbox_to_anchor=(0.8,-0.06),
            ncol=2)
        if closed: 
            plt.plot(closedPos, fog_ar[closedPos-1], 'rX', label='closed')
            plt.legend(loc=0, bbox_to_anchor=(0.8,-0.06),
            ncol=2)
        
        """draw sentiment compound graph"""
        plt.subplot(133)
        plt.title('Sentiment')
        comp_ar = np.array(comp)
        x = np.arange(1,xAxis+1, 1)
        plt.plot(x, comp_ar)
        if accepted: plt.plot(acceptedPos, comp_ar[acceptedPos-1], 'bs')
        if closed: plt.plot(closedPos, comp_ar[closedPos-1], 'rX')
        
        plt.suptitle('Post metrics:')
        plt.show()
    
    def get_closed_position(self, preds, closedDate):      
        """find the time span"""
        pos = 1
        for pred in preds:            
            #4 is creation date
            predDate = pred[4]
            #post got on same day but diff time closed (when post got closed on same day) 
            if predDate.date() == closedDate.date() and predDate.time() > closedDate.time():
                return max(pos-1, 0)
            #post got on another day closed
            if predDate.date() > closedDate.date():
                return max(pos-1, 0)
            pos += 1
                     
    def get_accepted_postition(self, preds, pId):
        #On position 2 is the accepted answer id  
        accId = self.dbc.get_post_with_id(pId)[2]
        #On postion 4 is the creation date
        answerCreationDate = self.dbc.get_answer_with_id(accId)[4]
        pos = 1
        for pred in preds:            
            #4 is creation date
            predDate = pred[4]
            #post got accepted on the same day 
            if predDate.date() == answerCreationDate.date() and predDate.time() > answerCreationDate.time():
                return max(pos-1, 0)
            #post got on another day accepted
            if predDate.date() > answerCreationDate.date():
                return max(pos-1, 0)
            
            pos += 1
        #the last version got accepted
        return pos-1 
if __name__ == '__main__': 
    eA = EvolutionAnalysis()