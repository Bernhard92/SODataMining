'''
Created on 13.02.2019

@author: bernhard
'''
from DBConnection import *
import csv

import matplotlib.pyplot as plt
import numpy as np

class AcceptedDataAnalysis(object):
    
    def __init__(self):
        self.changed_after_acc = 0
        self.not_changed_after_acc = 0
        
        self.readbility_changed = 0
        self.sentiment_changed = 0
        
        self.dbc = DBConnection()
        
        """Accepted posts"""
        self.id_file = open("../Texts/Data/accepted/acc_post_dpo.csv", "rb")
        
        self.changed_id_file = open("../Texts/Data/accepted/changed_id.csv", "rb")
        self.flesch_data_file = open("../Texts/Data/accepted/flesch_data.csv", "rb")
        self.fog_data_file = open("../Texts/Data/accepted/fog_data.csv", "rb")
        self.sent_data_file = open("../Texts/Data/accepted/sent_data.csv", "rb")
        
        #self.get_ids()
        #self.count_changed_after_acc()
        #self.count_metric_changed()
        #self.calc_difference()
        
        #self.id_file.close()
        
        """Not accepted posts"""
        self.nac_id_file = open("../Texts/Data/accepted/nacc_post_dpo.csv", "rb")
        
        self.nac_flesch_data_file = open("../Texts/Data/accepted/nac_flesch_data.csv", "rb")
        self.nac_fog_data_file = open("../Texts/Data/accepted/nac_fog_data.csv", "rb")
        self.nac_sent_data_file = open("../Texts/Data/accepted/nac_sent_data.csv", "rb")
        
        #self.get_nac_ids()
        #self.nac_calc_difference()
        
        
       
            
        self.box_plot(self.flesch_data_file, self.nac_flesch_data_file, "Flesch")
        self.box_plot(self.fog_data_file, self.nac_fog_data_file, "Fog")
        self.box_plot(self.sent_data_file, self.nac_sent_data_file, "Sentiment")
        
        
    
    def get_ids(self):
        post_ids = self.dbc.get_postids_from_posts_with_acc_answer_gone()
        writer = csv.writer(self.id_file)
        
        # take only post ids from posts with more than one version before accepted answer 
        for post_id in post_ids:
            question = self.dbc.get_post_with_id(post_id[0])
            answer = self.dbc.get_answer_with_id(question[2])
            
            if answer != None:
                answerDate = answer[4]
                c = 0
                preds = self.dbc.get_all_predecessors(post_id[0])
                for pred in preds:
                    if pred[4].date() < answerDate.date():
                        c+=1
                
                if c > 1:
                    writer.writerow(post_id)
            
            
           
            
        
    def get_nac_ids(self):
        post_ids = self.dbc.get_postids_from_posts_with_nacc_answer_gone()
        writer = csv.writer(self.nac_id_file)  
        
        for post_id in post_ids:
            writer.writerow(post_id)
            
        
    def count_changed_after_acc(self):
        reader = csv.reader(self.id_file)
        writer = csv.writer(self.changed_id_file)
    
        for row in reader:
            question = self.dbc.get_post_with_id(row[0])
            acc_answer = self.dbc.get_answer_with_id(question[2])
            
            questionDate = question[13]
            
            if acc_answer != None:
                answerDate = acc_answer[4]
                
                if questionDate.date() <= answerDate.date():
                    self.not_changed_after_acc = self.not_changed_after_acc + 1
                elif questionDate.date() > answerDate.date():
                    self.changed_after_acc = self.changed_after_acc + 1
                    writer.writerow(row)
                else: 
                    print "######"
                    print question
                    print "######"
            else: 
                print "------"
                print question
                print "------"
            
        print self.not_changed_after_acc
        print self.changed_after_acc
                      
                
    def calc_difference(self):
        reader = csv.reader(self.id_file)
        
        flesch_old = 0
        fog_old = 0
        sentiment_old = 0        
        
        flesch_diff = 0
        fog_diff = 0
        sentiment_diff = 0
        
        
        
        for row in reader:
            print row[0]
            question = self.dbc.get_post_with_id(row[0])
            answer = self.dbc.get_answer_with_id(question[2])
            
            """happens seven times, deleted answer"""
            if answer != None: 
                answerDate = self.dbc.get_answer_with_id(question[2])[4]
                preds = self.dbc.get_all_predecessors(row[0])
                
                
                """readability"""
                noValue = True
                for pred in preds: 
                    if pred[12] != None and pred[4].date() < answerDate.date():
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
                    if pred[19] != None and pred[4].date() < answerDate.date():
                        if noValue:
                            flesch_old = pred[19]
                            noValue = False
                        else:
                            sentiment_diff = sentiment_diff + pred[19] - sentiment_old
                            sentiment_old = pred[19]
        
                      
                print "Flesch diff: ", flesch_diff
                print "Fog diff: ", fog_diff
                print "sent diff: ", sentiment_diff
                        
                self.flesch_data_file.write(str(flesch_diff))
                self.flesch_data_file.write('\n')
                self.fog_data_file.write(str(fog_diff))
                self.fog_data_file.write('\n')
                self.sent_data_file.write(str(sentiment_diff))
                self.sent_data_file.write('\n')
                    
                    
                flesch_diff = 0
                fog_diff = 0
                sentiment_diff = 0
                
                
    def nac_calc_difference(self):
        reader = csv.reader(self.nac_id_file)
        
        flesch_old = 0
        fog_old = 0
        sentiment_old = 0        
        
        flesch_diff = 0
        fog_diff = 0
        sentiment_diff = 0
        
        for row in reader:
            print row[0]
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
        
            self.nac_flesch_data_file.write(str(flesch_diff))
            self.nac_flesch_data_file.write('\n')
            self.nac_fog_data_file.write(str(fog_diff))
            self.nac_fog_data_file.write('\n')
            self.nac_sent_data_file.write(str(sentiment_diff))
            self.nac_sent_data_file.write('\n')
            
            flesch_diff = 0
            fog_diff = 0
            sentiment_diff = 0
            
        
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
        plt.title('Has accepted answer')
        plt.boxplot(np.array(ac_data).astype(np.float))
        
        plt.subplot(122)
        plt.title('Has no accepted answer')
        plt.boxplot(np.array(nac_data).astype(np.float))
        
        plt.suptitle(data_descr)
        plt.show()
        
    
    def test(self):
        flesch_diff = 0
        fog_diff = 0
        sentiment_diff = 0
        preds = self.dbc.get_all_predecessors(3184672)
        
        
        i = 0
        while preds[i][12] == None: i+=1
        firstVersion = preds[i]
        
        j = len(preds)-1
        while preds[j][12] == None and j > i: j-=1
        lastVersion = preds[j]
        print firstVersion
        
        
        flesch_diff = flesch_diff + lastVersion[12] - firstVersion[12]
        fog_diff = fog_diff + lastVersion[13] - firstVersion[13]
        sentiment_diff = sentiment_diff + lastVersion[19] - firstVersion[19]
        
        print "Flesch diff: ", flesch_diff
        print "Fog diff: ", fog_diff
        print "sent diff: ", sentiment_diff
        
        
        
        
        
if __name__ == "__main__": 
    main = AcceptedDataAnalysis()