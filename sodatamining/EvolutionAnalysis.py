'''
Created on 17.12.2018

@author: bernhard
'''

import matplotlib.pyplot as plt
import numpy as np
from DBConnection import *
import csv

class EvolutionAnalysis(object):
    
    flesch_reading_ease = 12
    gunning_fog_index = 13
    compound = 19
    

    def __init__(self, localData=False):
        
        
        self.dbc = StaticData() if localData else DBConnection()
        
        self.pId = 15942975
        self.closedpId = 8799764
        
        self.closedpId2 = 12470206
        self.closedpId3 = 50232844
        
        self.acceptedId = 17261284
        
        
        #self.plot_graph_of(self.pId)
        #self.plot_graph_of(self.closedpId, True, True)
        
        #self.plot_graph_of(self.closedpId2, True)
        #self.plot_graph_of(self.closedpId3, True)
        
        #self.plot_graph_of(self.acceptedId, False, True)
        
        #self.plot_pHEntries('all', 1)
        #self.plot_pHEntries('closed')
        #self.plot_pHEntries('accepted')
        #self.plot_pHEntries('closedAccepted')
        
        self.plot_his_depth_distr()
        
    def plot_pHEntries(self, set, delete=0):
        """ plots the number of posthistory entries FOR EACH POST entry
        set = all, closed, accepted, closedAccepted"""

        
        if set == 'all': posts = self.dbc.list_of_evolution_steps('asc')
        elif set == 'closed': posts = self.dbc.list_of_closed_evolution_steps('asc')
        elif set == 'accepted': posts = self.dbc.list_of_accepted_evolution_steps('asc')
        elif set == 'closedAccepted': posts = self.dbc.list_of_closed_accepted_evolution_steps('asc')
        
        xAxis = len(posts)+1
        hisVersions = []
        
        for post in posts:
            #number of posthistory entries
            hisVersions.append(post[0])
        
        #delete the last n elements
        if(delete > 0): 
            xAxis -= delete
            del hisVersions[-delete]
        
        hisVersions_arr = np.array(hisVersions)
        x = np.arange(1, xAxis, 1)   
        plt.plot(x, hisVersions_arr, 'b.')
        plt.show()
        
    def plot_his_depth_distr(self):
        """plots the number of posts FOR EACH history DEPTH"""
        
        #get data from database
        historyDis = self.dbc.get_history_depth_distr()
        print historyDis
        
        xAxis = []
        yAxis = []
        
        for entry in historyDis: 
            xAxis.append(entry[0])
            yAxis.append(entry[1])
        
        x = np.array(xAxis)
        y = np.array(yAxis)
        plt.bar(x,y)
        plt.show()
        
    
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
        if closed: closedPos = self.get_closed_position(preds, self.dbc.get_closed_date(pId)[0])
            
        #The post got accepted at some point
        if accepted: acceptedPos = self.get_accepted_postition(preds, pId)
                    
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

class StaticData():
        
        def get_history_depth_distr(self):
            """number of history entrys, number of 
            posts with the number of history entries"""
            
            file = open("../Texts/depth_distr_all.csv", "rb")
            reader = csv.reader(file)
            
            data = []
            for row in reader:
                t = (int(row[0]), int(row[1]))                
                data.append(t)
            
            #print data
            return data



if __name__ == '__main__': 
    eA = EvolutionAnalysis(True)