from nltk.sentiment.vader import SentimentIntensityAnalyzer
import readability


text = """import mysql.connector
from mysql.connector import Error


class DBConnection:
        
    def __init__(self, db_name="sotorrent18_09"):
        self.db_name = db_name
        self.conn = self.connect()
         
    def connect(self):
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database=self.db_name,
                                           user='root',
                                           password=self.get_db_password())
            if conn.is_connected():
                print('Connected to MySQL database')
            return conn
        except Error as e:
            print(e) 
            
    def store_readability_metrics(self, id_, table, metrics):
        try:
            cursor = self.conn.cursor()
            query = "" UPDATE "" + table + ""  
                        SET
                        `kincaid` = %s, 
                        `ari` = %s,
                        `coleman_liau` = %s, 
                        `flesch_reading_ease` = %s,
                        `gunning_fog_index` = %s,
                        `smog_index` = %s,
                        `dale_chall` = %s
                        WHERE `id` = %s; ""
                            
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
            # accept the changes
            self.conn.commit()
            
        except Error as e:
            print(e) 
        
        finally:
            cursor.close()
        
    def get_number_of_entries(self, table):
        "" Gets number of posts in table ""
        try: 
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(1) FROM " + self.db_name + "." + table + ";")
            result = cursor.fetchone()
        except Error as e: 
            print(e) 
        finally:
            cursor.close()
            return result
    "
"""
text = "hello how are you?"

print(SentimentIntensityAnalyzer().polarity_scores(text))
print(readability.getmeasures(text, lang='en'))