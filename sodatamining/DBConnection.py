'''
Created on 3 Nov 2018

@author: Bernhard
'''
import mysql.connector
from mysql.connector import Error

class DBConnection:
        
    def __init__(self):
        self.conn = self.connect()
         
    def connect(self):
        """ Connect to MySQL database """
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='python_mysql',
                                           user='root',
                                           password='122133144')
            if conn.is_connected():
                print('Connected to MySQL database')
            return conn
        except Error as e:
            print(e)
     
        
    def get_post_with_id(self, id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM posts WHERE `id` = id")
     
            row = cursor.fetchone()
            
            while row is not None:
                print(row)
                row = cursor.fetchone()
     
        except Error as e:
            print(e)
            
        finally:
            cursor.close()
               
    def store_readability_score(self, id, score):
        print("")
        
    def get_number_of_posts(self):
        return 10
        
    def close_connection(self):
        self.conn.close() 
        
