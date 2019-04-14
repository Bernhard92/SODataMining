'''
Created on 14.12.2018

@author: bernhard
'''
from sodatamining.DBConnection import DBConnection

class OpenClosed(object):
    '''
    In this class we separate the posts between "open" and "closed" posts
    '''


    def __init__(self):
        dbc = DBConnection()
        #create a text file to export calculated results 
        file = open("../Texts/open_closed_results.txt", "w")
        
        print("------------")
        file.write("Closed posts:\n")
        results = dbc.get_closed_posts_stats()
        for result in results:
            file.write(str(result) + "\n")
        file.write("\nOpen posts: \n")
        results = dbc.get_open_posts_stats()
        for result in results:
            file.write(str(result) + "\n")
        file.write("\n\nNot accepted posts:\n")
        results = dbc.get_not_accepted_posts_stats()
        for result in results:
            file.write(str(result) + "\n")
        file.write("\nAccepted posts: \n")
        results = dbc.get_accepted_posts_stats()
        for result in results:
            file.write(str(result)+"\n")


if __name__=="__main__": 
    oc = OpenClosed()
        