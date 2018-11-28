'''
Created on 28.11.2018

@author: bernhard
'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from DBConnection import *


class MyClass(object):
    
    '''
    Makes a Sentiment analysis of the posts

    '''
    dbc = DBConnection()
    #dbc.add_sentiment_coumns('posts')
    
    hotel_rev = ["Great place to be when you are in Bangalore.",
                "The place was being renovated when I visited so the seating was limited."  ,
                "Loved the ambience, loved the food",
                "The food is delicious but not over the top.",
                "Service - Little slow, probably because too many people.",
                "The place is not easy to locate",
                "Mushroom fried rice was tasty"]
        
    sid = SentimentIntensityAnalyzer()
    for sentence in hotel_rev:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in ss:
            print ('{0}: {1}, '.format(k, ss[k]))
        print()
        
        