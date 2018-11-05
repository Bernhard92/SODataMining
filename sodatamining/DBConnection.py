'''
Created on 3 Nov 2018

@author: Bernhard
'''
import base64
import mysql.connector
from mysql.connector import Error

print mysql.connector.paramstyle

class DBConnection:
        
    def __init__(self):
        self.conn = self.connect()
         
    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='python_db',
                                           user='root',
                                           password = self.get_db_password())
            if conn.is_connected():
                print('Connected to MySQL database')
            return conn
        except Error as e:
            print(e)
     
        
    def get_post_text_with_id(self, id_):
        """ Gets the hole post entry form the posts table """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT text FROM python_db.posts WHERE `id` = " + str(id_) + ";")
            result = cursor.fetchone()
     
        except Error as e:
            print(e)
            
        finally:
            cursor.close()
            return result
               
    def store_readability_score(self, id_, score):
        print("")
        
    def get_number_of_posts(self):
        """ Gets number of posts in table """
        try: 
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM python_db.posts;")
            result = cursor.fetchone()
        except Error as e: 
            print(e)
        finally:
            cursor.close()
            return result
            
        
    def close_connection(self):
        self.conn.close() 
        
    def get_db_password(self):
        log_in_file = open("../.login_data")
        return base64.b64decode(log_in_file.readline())
    
    
    