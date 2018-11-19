'''
Created on 3 Nov 2018

@author: Bernhard
'''
import base64
import mysql.connector
from mysql.connector import Error
from bsddb.test.test_all import cursor_py3k


class DBConnection:
        
    def __init__(self, db_name="python_db"):
        self.db_name = db_name
        self.conn = self.connect()
        
         
    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host ='localhost',
                                           database = self.db_name,
                                           user ='root',
                                           password = self.get_db_password())
            if conn.is_connected():
                print 'Connected to MySQL database'
            return conn
        except Error as e:
            print(e)
     
    
    """ 
        readability measurements 
    
    """
        
    def get_post_text_with_id(self, id_):
        """ Gets the hole post entry form the posts table """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT text FROM " + self.db_name + ".posts WHERE `id` = " + str(id_) + ";")
            result = cursor.fetchone()
     
        except Error as e:
            print(e)
            
        finally:
            cursor.close()
            return result
               
    def store_readability_metrics(self, id_, metrics):
        """ Stores the calculated metrics directly in the posts table """
        try:
            cursor = self.conn.cursor()
            query = """ UPDATE `posts` 
                        SET
                        `kincaid` = %s, 
                        `ari` = %s,
                        `coleman_liau` = %s, 
                        `flesch_reading_ease` = %s,
                        `gunning_fog_index` = %s,
                        `smog_index` = %s,
                        `dale_chall` = %s
                        WHERE `id` = %s; """
                            
            data = (
                metrics['readability grades']['Kincaid'],
                metrics['readability grades']['ARI'],
                metrics['readability grades']['Coleman-Liau'], 
                metrics['readability grades']['FleschReadingEase'],
                metrics['readability grades']['GunningFogIndex'],
                metrics['readability grades']['SMOGIndex'],     
                metrics['readability grades']['DaleChallIndex'],        
                id_)
            
            cursor.execute(query, data)
            
            #accept the changes
            self.conn.commit()
            
        except Error as e:
            print(e)
        
        finally:
            cursor.close()
        
    def get_number_of_posts(self):
        """ Gets number of posts in table """
        try: 
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM " + self.db_name + ".posts;")
            result = cursor.fetchone()
        except Error as e: 
            print(e)
        finally:
            cursor.close()
            return result
            
    """
    Load data from Google BigQuery
    """
    
    

    
    
    
    
    """
    operational stuff
    """
    def close_connection(self):
        self.conn.close() 
        
    def get_db_password(self):
        log_in_file = open("../.login_data")
        return base64.b64decode(log_in_file.readline())
    
    
    