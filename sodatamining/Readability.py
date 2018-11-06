import readability
from DBConnection import *

class Readability:
    
    def __init__(self):
        self._dbConnection = DBConnection() 
        n_posts = self.number_db_entries()
        print "Number of entries: ", n_posts, "\n"
        
        for id_ in range(1, n_posts+1):
            """ For every entry in the database """ 
            
            #Gets text from text block of post
            text = self.get_text_from_post(id_)
            
            #Calculates the metrics of the text
            results = self.calc_metrics_of_post(text)
            
            #Print the metrics in stdout 
            self.print_readability_metrics(results)
            
            #Stores the metrics in the database
            self.store_readability_metrics(id_, results)
            
            
        
 
    def get_text_from_post(self, id_):
        """ Gets the text of the post in a tuple
            and returns only the text as string """
        return self._dbConnection.get_post_text_with_id(id_)[0]
    
    def calc_metrics_of_post(self, text):
        """ Returns a dictionary of measurements
        consisting of:  
                        readability grades
                        sentence info
                        word usage
                        sentence beginnings """ 
                        
        print("Calculating the metrics of: " + text)
        return readability.getmeasures(unicode(text), lang='en')
    
    def number_db_entries(self):
        """Get Number of entries form post table"""
        return self._dbConnection.get_number_of_posts()[0]
    
    def store_readability_metrics(self, id_, results):
        self._dbConnection.store_readability_metrics(id_, results)


    def print_readability_metrics(self, results):
        print"Kinacaid: ", results['readability grades']['Kincaid']
        print"ARI: ",results['readability grades']['ARI']
        print"Coleman-Liau: ", results['readability grades']['Coleman-Liau']
        print"Flesch reading ease: ", results['readability grades']['FleschReadingEase']
        print"Gunning Fog Index: ", results['readability grades']['GunningFogIndex']
        print"LIX: ", results['readability grades']['LIX']
        print"SMOG Index: ", results['readability grades']['SMOGIndex']
        print"RIX: ", results['readability grades']['RIX'], "\n"
        
        
        
        
if __name__ == "__main__":
    rdb = Readability()
