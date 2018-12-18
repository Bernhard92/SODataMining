'''
Created on 10.12.2018

@author: bernhard
'''
import csv 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from _ast import Tuple

class NLTKCheck():

    def __init__(self):
        self.posValues = 0
        self.neuValues = 0
        self.negValues = 0
        
        self.falsePosValues = 0
        self.falesNeuValues = 0
        self.falseNegValues = 0
        
        self.correctPosValues = 0
        self.correctNeuValues = 0
        self.correctNegValues = 0
        
        self.correct = 0
        self.false = 0
        
        self.csvFile = open('StackOverflow.csv')
        csvReader = csv.reader(self.csvFile, delimiter=',')
        
        correctComp = []
        comp = []
        
        lineCount = 0
        for row in csvReader:
            if lineCount != 0: 
                self.count_values(row[2])
                correctComp.append(row[2])
                comp.append(self.calc_sentiment(row[1]))
            
            lineCount += 1
        
        
        
        print 'Positive values ' + str(self.posValues)
        print 'Neutral values ' + str(self.neuValues)
        print 'Negative values ' + str(self.negValues)
        print
        
        
        neutral_range = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        
        
        for neuRange in neutral_range:
            print "Neutral range: " + str(neuRange)
            self.reset_values()
            
            for i in range(0, len(comp)):
                
                cat_comp = str(self.categorize_sentiment(comp[i], neuRange))
                
                if cat_comp == correctComp[i]:
                    self.correct += 1
                else: 
                    self.false +=1 
               
            print 'False: ' + str(self.false)
            print 'Correct: ' + str(self.correct)
           
            print '---------------------------'
            
            
            
            
        
    def calc_sentiment(self, text):    
        sid = SentimentIntensityAnalyzer()
        return sid.polarity_scores(text)['compound']
             
    
    def categorize_sentiment(self, value, neuRange):
        if (value < (neuRange * -1)):
            return -1
        elif (value > neuRange): 
            return 1
        else:
            return 0 
        
    def count_values(self, value): 
        if value == str(-1): 
            self.negValues += 1
        elif value == str(1):
            self.posValues += 1
        elif value == str(0): 
            self.neuValues += 1 
            
    def reset_values(self):
        self.posValues = 0
        self.neuValues = 0
        self.negValues = 0
        
        self.falsePosValues = 0
        self.falesNeuValues = 0
        self.falseNegValues = 0
        
        self.correctPosValues = 0
        self.correctNeuValues = 0
        self.correctNegValues = 0
        
        self.correct = 0
        self.false = 0
        
      
        
if __name__ == '__main__':
    nltkCheck = NLTKCheck()