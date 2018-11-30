'''
Created on 28.11.2018

@author: bernhard
'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from DBConnection import *


class Sentiment(object):
    
    '''
    Makes a Sentiment analysis of the posts

    '''
    
    def __init__(self):
        self.dbc = DBConnection()
        self.postBlockVersionAltered = True
        self.postHistoryAltered = True
        self.postsAltered = True
        self.commentsAltered = True
        
        # calculates sentiment score of all text blocks
        self.postblockversion_sentiment()
        
        # calculates sentiment score of text blocks from history entries
        #self.posthistory_sentiment()
        
        # calculates sentiment score of most recent post versions
        #self.posts_sentiment()
        
        # calculates sentiment score of the post comments
        #self.comment_sentiment()
        
    def postblockversion_sentiment(self):
        # alter posts table: add metric columns
        if (not self.postBlockVersionAltered):
            self.dbc.add_sentiment_columns("postblockversion")
   
        """ For every entry in the database """
        
        entries = self.dbc.get_id_content_from_postblockversion()
        
        counter = 0
        for entry in entries:
            # id from table entry
            id_ = entry[0]
            
            # Calculates the metrics of the text
            results = self.calc_sentiment(entry[1])
            
            if (results != 0):
                # Print the metrics in stdout 
                #self.print_sentiment(results)
                
                # Stores the metrics in the database
                self.dbc.store_sentiment(id_, "postblockversion", results)
              
            counter += 1
            if counter % 10000 == 0:
                print str(counter) + ' statements executed!'
        
    def posthistory_sentiment(self): 
        # adds the columns for the sentiment 
        # analysis to the posthistory table  
        if (not self.postHistoryAltered): 
            self.dbc.add_sentiment_columns('posthistory')
            
        count = 0
        phIds = self.dbc.get_ids_from_posthistory()
        
        for id_ in phIds:                
            # get all textblocks from the posthistory entry
            try: 
                textblocks = self.dbc.get_content_from_posthistory(id_[0])
                # get all the text blocks from the history version of the post
                text = ""
                for block in textblocks:
                    text = text + "\n" + block[0]
                
                # Calculates the metrics of the text
                results = self.calc_sentiment(text)
                if (results != 0):
                    # Print the metrics in stdout 
                    # self.print_sentiment(results)
                    
                    # Stores the metrics in the database
                    self.dbc.store_sentiment(id_[0], "posthistory", results)
            except UnboundLocalError:
                print "No post block verion"
                continue
            
            count += 1
            if count % 10000 == 0:
                print str(count) + " statements executed!"
                
    def posts_sentiment(self):
        # adds the columns for the sentiment analysis to the posts table
        if (not self.postsAltered):
            self.dbc.add_sentiment_columns('posts')
            
        results = self.dbc.get_most_recent_sentiment()
        count = 0
        for result in results:
            count += 1
            if count % 10000 == 0:
                print "10.000 querys executed!"
                
            # post id
            id_ = result[0]
            # sentiment metrics
            metrics = {'neg': result[1],
                       'neu': result[2],
                       'pos': result[3],
                       'compound': result[4]
                       }
   
            # store in posts table
            #print id_
            #print metrics
            self.dbc.store_sentiment(id_, "posts", metrics)
       
    def comment_sentiment(self):
        # adds the columns for the sentiment analysis to the comments table
        if (not self.commentsAltered):
            self.dbc.add_sentiment_columns('comments')
        
        comments = self.dbc.get_comment_text()
        count = 0
        for comment in comments:
            
            id_ = comment[0]
            result = self.calc_sentiment(comment[1])
        
            #print id_
            #print result 
            
            self.dbc.store_sentiment(id_, 'comments', result)
            
            count += 1
            if count % 10000 == 0: 
                print str(count) + ' Comments done!'
            
        
    def calc_sentiment(self, text):    
        # in the csv files are these unconverted special chars
        text = text.replace('&#xD;&#xA;', '\n')  
        sid = SentimentIntensityAnalyzer()
        return sid.polarity_scores(text)
    
    def print_sentiment(self, result):
        for k in result:
            print ('{0}: {1}, '.format(k, result[k])) 
        

if __name__ == "__main__":
    sntm = Sentiment()
