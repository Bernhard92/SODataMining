import readability
from DBConnection import *

class Readability:
    
    def __init__(self):
        self._dbConnection = DBConnection() 
        n_posts = self.number_db_entries()
        for i in range(0, n_posts):
            post = self.get_post_from_db(i)
        # print(results['readability grades']['FleschReadingEase'])
 
    def get_post_from_db(self, id):
        self._dbConnection.get_post_with_id(id)
    
    def calc_score_of_post(self, post):
        results = readability.getmeasures(unicode(post), lang='en')
    
    def number_db_entries(self):
        """Get Number of entries form post table"""
        return self._dbConnection.get_number_of_posts()
    
    def store_rb_score(self, id, score):
        self._dbConnection.store_readability_score(id, score)


rdb = Readability()
