from DBConnection import *


class PostEvolution:
    
    def __init__(self):
        self.debug = False
        self.dbc = DBConnection()
        
        # creates the two tables that hold the differences from one version to another
        #self.dbc.create_evolution_tables()
        
        # calculates and writes the evolutionary steps of the 
        # post blocks into postblockevolution 
        #self.postblock_evolution()
        
        # calculates and writes the evolutionary steps of 
        # post history into posthistoryevolution 
        self.posthistory_evolution()
    
    def postblock_evolution(self):
        counter = 0
        # gets the id's of all entries of the table
        post_block_ids = self.dbc.get_ids_from_postblockversion()
        
        for id_ in post_block_ids:
            # block contains: posthistoryid, postblockid, predpostblockid, 
            # flesch_reading_ease, gunning fog index, neg, neu, pos, compound 
            block = self.dbc.get_postblock_value(id_[0])
            predBlock = self.dbc.get_postblock_value(block[2])
            
            if predBlock != None:
                self.evaluate_evolution('postblockevolution', block, predBlock)
            #else: 
                #print str(id_) + ' has no predecessor!'
                
            counter += 1
            if ((counter % 10000) == 0):
                print str(counter) + " post blocks processed!"
                                
    def posthistory_evolution(self):
        counter = 0
        post_history_ids = self.dbc.get_posthistoryid_from_texttype()
        
        for id_ in post_history_ids: 
            # post contains: placeholder, posthistoryid, predposthistoryid, 
            # flesch_reading_ease, gunning fog index, neg, neu, pos, compound 
            post = self.dbc.get_posthistory_value(id_[0])
            # predPost contains: placeholder, placeholder2, posthistoryid,
            # flesch_reading_ease, gunning fog index, neg, neu, pos, compound 
            predPost = self.dbc.get_predposthistory_value(post[2])    
            
            if predPost != None: 
                self.evaluate_evolution('posthistoryevolution', post, predPost)
            #else: 
                #print str(id_) + ' has no predecessor!'
                
            counter += 1
            if ((counter % 10000) == 0):
                print str(counter) + " history posts processed!"
                    
    def evaluate_evolution(self, table, entry, predEntry):
        change_type = ''
        debugString = ''
            
        """Flesch-Reading-Ease compairement"""
        if entry[3] > predEntry[3]:
            # Higher score means easier to read
            change_type = 'readability_flesch_improved'
        elif entry[3] < predEntry[3]:
            change_type = 'readability_flesch_aggravate'
        else:
            change_type = 'readability_flesch_unchanged'
               
        if not self.debug:
            self.insert_evolution_entry(table, entry, predEntry, change_type, entry[3], predEntry[3])
        else: 
            debugString += change_type + "-"
            
        """Gunning_Fox index"""
        if entry[4] < predEntry[4]:
            # Lower score means easier to read
            change_type = 'readability_fog_improved'
        elif entry[4] > predEntry[4]: 
            change_type = 'readability_fog_aggravate'
        else: 
            change_type = 'readability_fog_unchanged'
        
        if not self.debug:         
            self.insert_evolution_entry(table, entry, predEntry, change_type, entry[4], predEntry[4])
        else: 
            debugString += change_type + "-"
            
        """
        \"""Sentiment negative value\"""
        if entry[5] < predEntry[5]:
            change_type = 'sentiment_neg_decreased'
        else: 
            change_type = 'sentiment_neg_increased'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[5], predEntry[5])
        
        \"""Sentiment neutral value\"""
        if entry[6] < predEntry[6]:
            change_type = 'sentiment_neu_decreased'
        else: 
            change_type = 'sentiment_neu_increased'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[6], predEntry[6])
        
        \"""Sentiment positive value\"""
        if entry[7] < predEntry[7]:
            change_type = 'sentiment_pos_decreased'
        else: 
            change_type = 'sentiment_pos_increased'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[7], predEntry[7])
        """
        
        """Sentiment compound value"""
        if entry[8] > predEntry[8]:
            change_type = 'sentiment_com_improved'
        elif entry[8] < predEntry[8]: 
            change_type = 'sentiment_com_aggravate'
        else: 
            change_type = 'sentiment_com_unchanged'
            
        if not self.debug:        
            self.insert_evolution_entry(table, entry, predEntry, change_type, entry[8], predEntry[8])
        else: 
            debugString += change_type
            return debugString
        
    def insert_evolution_entry(self, table,  entry, predEntry, change_type, vnew, vold):
        
        if table == 'postblockevolution':
            values = {
                    'posthistoryid': entry[0],
                    'changetype': change_type,
                    'postblockid': entry[1],
                    'predpostblockid': predEntry[1],
                    'valuenew': vnew,
                    'valueold': vold
                    }
        
            if self.debug:
                return values;
            else:
                self.dbc.insert_postblockevolution_entry(values)
                        
        elif table == 'posthistoryevolution': 
            values = {
                    'changetype': change_type,
                    'posthistoryid': entry[1],
                    'predposthistoryid': predEntry[2],
                    'valuenew': vnew,
                    'valueold': vold
                    }
            
            if self.debug:
                return values
            else:
                self.dbc.insert_posthistoryevolution_entry(values)
        
if __name__ == "__main__":
    pE = PostEvolution()