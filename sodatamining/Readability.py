import readability
from DBConnection import *


class Readability:   
    
    def __init__(self):
        self._dbConnection = DBConnection() 
        #set false to add readability columns to PostBlockVersion
        self._postBlockVersionAltered = True
        #set false to add readability columns to PostHistory
        self._postHistoryAltered = True
        self._counter = 0
        
        #create indices for the sotorrent database
        #self._dbConnection.create_indices()
        
        #add readability measures to blocks 
        #self.postblockversion_readability()
        
        #add readability measures to posthistory 
        self.posthistory_readability()
    
    
    def calc_metrics_of_post(self, id_, text):
        """ Returns a dictionary of measurements
        consisting of:  
                        readability grades
                        sentence info
                        word usage
                        sentence beginnings """ 
        
        #in the csv files are these unconverted special chars
        text = text.replace('&#xD;&#xA;', '\n')  
        
        self._counter += 1 
        if(self._counter % 10000 == 0):
            print id_
        # print("Calculating the metrics of: Id: "+ str(id_) +" Text: "+ text)
        try: 
            return readability.getmeasures(unicode(text), lang='en')
        except ValueError as e:
            return 0
    
    def number_db_entries(self, table):
        """Get Number of entries form post table"""
        return self._dbConnection.get_number_of_entries(table)[0]

    def print_readability_metrics(self, results):
        print"Kinacaid: ", results['readability grades']['Kincaid']
        print"ARI: ", results['readability grades']['ARI']
        print"Coleman-Liau: ", results['readability grades']['Coleman-Liau']
        print"Flesch reading ease: ", results['readability grades']['FleschReadingEase']
        print"Gunning Fog Index: ", results['readability grades']['GunningFogIndex']
        print"SMOG Index: ", results['readability grades']['SMOGIndex']
        print"Dale-Chall: ", results['readability grades']['DaleChallIndex'], "\n" 
      
    def postblockversion_readability(self):
        # alter posts table: add metric columns
        if (not self._postBlockVersionAltered):
            self._dbConnection.add_readability_columns("postblockversion")
   
        """ For every entry in the database """
        
        entries = self._dbConnection.get_id_content_from_postblockversion()
        
        for entry in entries:
            # id from table entry
            id_ = entry[0]
            
            # Calculates the metrics of the text
            results = self.calc_metrics_of_post(id_, entry[1])
            
            if (results != 0):
                # Print the metrics in stdout 
                # self.print_readability_metrics(results)
                
                # Stores the metrics in the database
                self._dbConnection.store_readability_metrics(id_, "postblockversion", results)
              
    def posthistory_readability(self):
        if (not self._postHistoryAltered):
            self._dbConnection.add_readability_columns("posthistory")
        
        phIds = self._dbConnection.get_ids_from_posthistory()
        for id_ in phIds:
            # get all textblocks from the posthistory entry
            try: 
                print id_[0]
                textblocks = self._dbConnection.get_content_from_posthistory(id_[0])
                print len(textblocks)
                print textblocks
            except UnboundLocalError as e:
                #print "No post block verion"
                continue

        
if __name__ == "__main__":
    rdb = Readability()

