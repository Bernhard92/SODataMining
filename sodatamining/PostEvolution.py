from DBConnection import *


class PostEvolution:
    
    def __init__(self):
        self.dbc = DBConnection()
        
        # creates the two tables that hold the differences  from one version to another
        #self.dbc.create_evolution_tables()
    
    def postblock_evolution(self):
        
        # gets the id´s of all entries of the table
        post_block_ids = self.dbc.get_ids_from_postblockversion()
        
        for id_ in post_block_ids:
            # block contains: posthistoryid, postblockid, predpostblockid, 
            # flesch_reading_ease, gunning fog index, neg, neu, pos, compound 
            block = self.dbc.get_postblock_value(id_)
            predBlock = self.dbc.get_postblock_value(block[2])
            
            if predBlock != None:
                self.evaluate_evolution('postblockevolution', block, predBlock)
            else: 
                print str(id_) + ' has no predecessor!'
          
    def posthistory_evolution(self):
       
        post_history_ids = self.dbc.get_ids_from_posthistory() 
        
        for id_ in post_history_ids: 
            # post contains: placeholder, posthistoryid, predposthistoryid, 
            # flesch_reading_ease, gunning fog index, neg, neu, pos, compound 
            post = self.dbc.get_posthistory_value(id_)
            # predPost contains: placeholder, placeholder2, posthistoryid,
            # flesch_reading_ease, gunning fog index, neg, neu, pos, compound 
            predPost = self.dbc.get_predposthistory_value(post[1])    
            
            if predPost != None: 
                self.evaluate_evolution('posthistoryevolution', post, predPost)
            else: 
                print str(id_) + ' has no predecessor!'
                    
    def evaluate_evolution(self, table, entry, predEntry):
        change_type = ''
            
        """Flesch-Reading-Ease compairement"""
        if entry[3] > predEntry[3]:
            # Higher score means easier to read
            change_type = 'readability_Flesch_improved'
        else: 
            change_type = 'readability_Flesch_aggravate'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[3], predEntry[3])
        
        """Gunning_Fox index"""
        if entry[4] < predEntry[4]:
            # Lower score means easier to read
            change_type = 'readability_fox_improved'
        else: 
            change_type = 'readability_fox_aggravate'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[4], predEntry[4])
        
        """Sentiment negative value"""
        if entry[5] < predEntry[5]:
            change_type = 'sentiment_neg_decreased'
        else: 
            change_type = 'sentiment_neg_increased'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[5], predEntry[5])
        
        """Sentiment neutral value"""
        if entry[6] < predEntry[6]:
            change_type = 'sentiment_neu_decreased'
        else: 
            change_type = 'sentiment_neu_increased'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[6], predEntry[6])
        
        """Sentiment positive value"""
        if entry[7] < predEntry[7]:
            change_type = 'sentiment_pos_decreased'
        else: 
            change_type = 'sentiment_pos_increased'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[7], predEntry[7])
        
        
        """Sentiment compound value"""
        if entry[8] > predEntry[8]:
            change_type = 'sentiment_com_improved'
        else: 
            change_type = 'sentiment_com_aggravate'
                  
        self.insert_evolution_entry(table, entry, predEntry, change_type, entry[8], predEntry[8])
         
    def insert_evolution_entry(self, table,  entry, predEntry, change_type, vnew, vold):
        if table == 'postblockevolution':
            values = {
                    'posthistoryid': entry[0],
                    'changetype': change_type,
                    'postblockid': entry[1],
                    'predpostblockid': entry[2],
                    'valuenew': vnew,
                    'valueold': vold
                    }
            self.dbc.insert_evolution_entry(values)
        
        elif table == 'posthistoryevolution': 
            values = {
                    'changetype': change_type,
                    'postblockid': entry[1],
                    'predpostblockid': entry[2],
                    'valuenew': vnew,
                    'valueold': vold
                    }
            self.dbc.insert_evolution_entry(values)
        
        
