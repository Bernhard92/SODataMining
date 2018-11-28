import readability
from DBConnection import *


class Readability:   
    
    def __init__(self):
        self._dbConnection = DBConnection() 
        # set false to add readability columns to PostBlockVersion
        self._postBlockVersionAltered = True
        # set false to add readability columns to PostHistory
        self._postHistoryAltered = True
        # set false to add readability columns to Posts
        self._postsAltered = True
        
        # create indices for the sotorrent database
        # self._dbConnection.create_indices()
        
        # add readability measures to blocks 
        # self.postblockversion_readability()
        
        # add readability measures to posthistory 
        # self.posthistory_readability()
        
        #add readability measures to posts
        self.posts_readability()
    
    def calc_metrics_of_post(self, text):
        """ Returns a dictionary of measurements
        consisting of:  
                        readability grades
                        sentence info
                        word usage
                        sentence beginnings """ 
        
        # in the csv files are these unconverted special chars
        text = text.replace('&#xD;&#xA;', '\n')  
        
        # print("Calculating the metrics of: Id: "+ str(id_) +" Text: "+ text)
        try: 
            return readability.getmeasures(unicode(text), lang='en')
        except ValueError:
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
            results = self.calc_metrics_of_post(entry[1])
            
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
                textblocks = self._dbConnection.get_content_from_posthistory(id_[0])
                
                #get all the text blocks from the history version of the post
                text = ""
                for block in textblocks:
                    text = text + "\n" + block[0]
                
                #Calculates the metrics of the text
                results = self.calc_metrics_of_post(text)
                if (results != 0):
                    #Print the metrics in stdout 
                    #self.print_readability_metrics(results)
                    
                    #Stores the metrics in the database
                    self._dbConnection.store_readability_metrics(id_[0], "posthistory", results)
            except UnboundLocalError:
                print "No post block verion"
                continue

    def posts_readability(self):
        if (not self._postHistoryAltered):
            self._dbConnection.add_readability_columns("posts")
            
        results = self._dbConnection.get_most_recent_score()
        count = 0
        for result in results:
            count += 1
            if count % 10000 == 0:
                print "10.000 querys executed!"
                
            #post id
            id_ = result[0]
            #readability metrics
            metrics = {'readability grades': 
                       {'Kincaid': result[1],
                        'ARI': result[2],
                        'Coleman-Liau': result[3], 
                        'FleschReadingEase': result[4], 
                        'GunningFogIndex': result[5], 
                        'SMOGIndex' : result[6], 
                        'DaleChallIndex' : result[7]
                        }
                       }
        
   
            #metrics = ['readability grades'][result[1:]]
            #store in posts table
            #print id_
            #print metrics
            self._dbConnection.store_readability_metrics(id_, "posts", metrics)
        
if __name__ == "__main__":
    rdb = Readability()

