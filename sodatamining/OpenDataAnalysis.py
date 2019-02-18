'''
Created on 15.02.2019

@author: bernhard
'''

from DBConnection import *
import csv
import matplotlib.pyplot as plt
import numpy as np

class OpenDataAnalysis(object):
    
    def __init__(self):
        self.dbc = DBConnection()
        
        #self.open_id()
        #self.closed_id()
        
        #self.calc_open_diff()
        #self.calc_closed_diff()
        
        self.box_plot(open("../Texts/Data/open/open_flesch_data.csv", "rb"), 
                      open("../Texts/Data/open/closed_flesch_data.csv", "rb"), 
                      "Flesch")
        
        self.box_plot(open("../Texts/Data/open/open_fog_data.csv", "rb"), 
                      open("../Texts/Data/open/closed_fog_data.csv", "rb"), 
                      "Fog")
        
        self.box_plot(open("../Texts/Data/open/open_sent_data.csv", "rb"), 
                      open("../Texts/Data/open/closed_sent_data.csv", "rb"), 
                      "Sentiment")
        """
        
        self.scatter_plot(open("../Texts/Data/open/open_flesch_data.csv", "rb"), 
                      open("../Texts/Data/open/closed_flesch_data.csv", "rb"))
        
        """
        #self.hist_plot(open("../Texts/Data/open/open_flesch_data.csv", "rb"), 
                        #open("../Texts/Data/open/closed_flesch_data.csv", "rb"))
                        
        #self.count_closed_diff()
    
    def open_id(self):
        open_ip_file = open("../Texts/Data/open/open_id.csv", "wb")
        openPosts = self.dbc.get_open_posts_gone()
        
        for post in openPosts:
            open_ip_file.write(str(post[0]))
            open_ip_file.write('\n')
            
        
    def closed_id(self):
        closed_ip_file = open("../Texts/Data/open/closed_id.csv", "wb")
        closedPosts = self.dbc.get_closed_posts_gone()
        
        for post in closedPosts:
            preds = self.dbc.get_all_predecessors(post[0])
            print post 
            closedDate = post[1]
            
            c = 0
            for pred in preds: 
                if pred[4].date() < closedDate.date():
                    c+=1
        
            if c > 1:
                closed_ip_file.write(str(post[0]))
                closed_ip_file.write('\n')
    
    
    def calc_open_diff(self):
        reader = csv.reader(open("../Texts/Data/open/open_id.csv", "rb"))
        open_flesch_data = open("../Texts/Data/open/open_flesch_data.csv", "wb")
        open_fog_data = open("../Texts/Data/open/open_fog_data.csv", "wb")
        open_sent_data = open("../Texts/Data/open/open_sent_data.csv", "wb")
        
        flesch_old = 0
        fog_old = 0
        sentiment_old = 0        
        
        flesch_diff = 0
        fog_diff = 0
        sentiment_diff = 0
        
        for row in reader:
            preds = self.dbc.get_all_predecessors(row[0])
            
            """readability"""
            noValue = True
            for pred in preds: 
                if pred[12] != None:
                    if noValue:
                        flesch_old = pred[12]
                        fog_old = pred[13]
                        noValue = False
                    else:
                        flesch_diff = flesch_diff + pred[12] - flesch_old
                        flesch_old = pred[12]
                        
                        fog_diff = fog_diff + pred[13] - fog_old
                        fog_old = pred[13]
            
            """sentiment"""
            noValue = True
            for pred in preds: 
                if pred[19] != None:
                    if noValue:
                        flesch_old = pred[19]
                        noValue = False
                    else:
                        sentiment_diff = sentiment_diff + pred[19] - sentiment_old
                        sentiment_old = pred[19]
            
                  
            print "Flesch diff: ", flesch_diff
            print "Fog diff: ", fog_diff
            print "sent diff: ", sentiment_diff
        
            open_flesch_data.write(str(flesch_diff))
            open_flesch_data.write('\n')
            open_fog_data.write(str(fog_diff))
            open_fog_data.write('\n')
            open_sent_data.write(str(sentiment_diff))
            open_sent_data.write('\n')
            
            flesch_diff = 0
            fog_diff = 0
            sentiment_diff = 0
            
    def calc_closed_diff(self):
        reader = csv.reader(open("../Texts/Data/open/closed_id.csv", "rb"))
        closed_flesch_data = open("../Texts/Data/open/closed_flesch_data.csv", "wb")
        closed_fog_data = open("../Texts/Data/open/closed_fog_data.csv", "wb")
        closed_sent_data = open("../Texts/Data/open/closed_sent_data.csv", "wb")
        
        flesch_old = 0
        fog_old = 0
        sentiment_old = 0        
        
        flesch_diff = 0
        fog_diff = 0
        sentiment_diff = 0
        
               
        for row in reader:
            closedDate = self.dbc.get_post_with_id(row[0])[20]
            preds = self.dbc.get_all_predecessors(row[0])
            
            
            """readability"""
            noValue = True
            for pred in preds: 
                if pred[12] != None and pred[4].date() < closedDate.date():
                    if noValue:
                        flesch_old = pred[12]
                        fog_old = pred[13]
                        noValue = False
                    else:
                        flesch_diff = flesch_diff + pred[12] - flesch_old
                        flesch_old = pred[12]
                        
                        fog_diff = fog_diff + pred[13] - fog_old
                        fog_old = pred[13]
        
            """sentiment"""
            noValue = True
            for pred in preds: 
                if pred[19] != None and pred[4].date() < closedDate.date():
                    if noValue:
                        flesch_old = pred[19]
                        noValue = False
                    else:
                        sentiment_diff = sentiment_diff + pred[19] - sentiment_old
                        sentiment_old = pred[19]
    
                  
            print "Flesch diff: ", flesch_diff
            print "Fog diff: ", fog_diff
            print "sent diff: ", sentiment_diff
                    
            closed_flesch_data.write(str(flesch_diff))
            closed_flesch_data.write('\n')
            closed_fog_data.write(str(fog_diff))
            closed_fog_data.write('\n')
            closed_sent_data.write(str(sentiment_diff))
            closed_sent_data.write('\n')
                                    
            flesch_diff = 0
            fog_diff = 0
            sentiment_diff = 0
     
    def count_closed_diff(self):
        reader = csv.reader(open("../Texts/Data/open/closed_id.csv", "rb"))
        
        flesch_old = 0
        fog_old = 0
        sentiment_old = 0        
        
        flesch_diff = 0
        fog_diff = 0
        sentiment_diff = 0
        
        flesch_diff_total = 0
        fog_diff_total = 0
        sent_diff_total = 0
        
               
        for row in reader:
            closedDate = self.dbc.get_post_with_id(row[0])[20]
            preds = self.dbc.get_all_predecessors(row[0])
            
            
            """readability"""
            noValue = True
            for pred in preds: 
                if pred[12] != None and pred[4].date() < closedDate.date():
                    if noValue:
                        flesch_old = pred[12]
                        fog_old = pred[13]
                        noValue = False
                    else:
                        flesch_diff = flesch_diff + pred[12] - flesch_old
                        flesch_old = pred[12]
                        
                        fog_diff = fog_diff + pred[13] - fog_old
                        fog_old = pred[13]
        
            """sentiment"""
            noValue = True
            for pred in preds: 
                if pred[19] != None and pred[4].date() < closedDate.date():
                    if noValue:
                        flesch_old = pred[19]
                        noValue = False
                    else:
                        sentiment_diff = sentiment_diff + pred[19] - sentiment_old
                        sentiment_old = pred[19]
    
                  
            print "Flesch diff: ", flesch_diff
            print "Fog diff: ", fog_diff
            print "sent diff: ", sentiment_diff
                    
            if flesch_diff != 0:
                flesch_diff_total += 1
            if fog_diff != 0:
                fog_diff_total += 1
            if sentiment_diff != 0:
                sent_diff_total += 1
                                    
            flesch_diff = 0
            fog_diff = 0
            sentiment_diff = 0
            
        print 'Flesch total diff: ', flesch_diff_total
        print 'Fog total diff: ', fog_diff_total
        print 'Sent total diff: ', sent_diff_total
            
    def box_plot(self, data_ac, data_nac, data_descr):
        ac_reader = csv.reader(data_ac)
        nac_reader = csv.reader(data_nac)
        
        ac_data = []
        nac_data = []
        
        for row in ac_reader:
            ac_data.append(row[0])
            
        for row in nac_reader:
            nac_data.append(row[0])
            
        plt.figure(1, figsize=(12,5))
        
        ax = plt.subplot(121)
        plt.title('Open')
        plt.boxplot(np.array(ac_data).astype(np.float))
        
        plt.subplot(122)
        plt.title('Closed')
        plt.boxplot(np.array(nac_data).astype(np.float))
        
        plt.suptitle(data_descr)
        plt.show()
      
    def scatter_plot(self, open_data, closed_data):
        open_reader = csv.reader(open_data)
        closed_reader = csv.reader(closed_data)
        
        o_data = []
        c_data = []
        
        for row in open_reader:
            o_data.append(float(row[0]))
            
        for row in closed_reader:
            c_data.append(float(row[0]))
        
        
        plt.figure(1, figsize=(12,5))
        
        plt.subplot(121)
        plt.title('Open')
        plt.scatter(range(0,len(o_data)), o_data)
        
        plt.subplot(122)
        plt.title('Closed')
        plt.scatter(range(0,len(c_data)), c_data)
        
        plt.show()
        
    def hist_plot(self, open_data, closed_data):
        open_reader = csv.reader(open_data)
        closed_reader = csv.reader(closed_data)
        
        o_data = []
        c_data = []
        
        for row in open_reader:
            o_data.append(float(row[0]))
            
        for row in closed_reader:
            c_data.append(float(row[0]))
        
        mu = 0
        sigma = 10
        
        plt.figure(1, figsize=(12,5))
        
        x = mu + sigma * np.array(o_data)
        plt.subplot(121)
        plt.title('Open')
        # the histogram of the data
        plt.hist(x, 20, density=1, facecolor='g', alpha=0.75)
        
        
        x = mu + sigma * np.array(c_data)
        plt.subplot(122)
        plt.title('Closed')
        # the histogram of the data
        plt.hist(x, 20, density=1, facecolor='g', alpha=0.75)
       
        
        plt.show()
    
        
if __name__ == '__main__':
    oda = OpenDataAnalysis()