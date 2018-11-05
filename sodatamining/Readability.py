import readability
from DBConnection import *

class Readability:
    
    def __init__(self):
        self._dbConnection = DBConnection() 
        n_posts = self.number_db_entries()
        print("Number of entries: ", n_posts)
        
        for id_ in range(1, n_posts+1):
            text = self.get_text_from_post(id_)
            results = self.calc_score_of_post(text)
            print(results['readability grades']['FleschReadingEase'])
        
 
    def get_text_from_post(self, id_):
        """ Gets the text of the post in a tuple
            and returns only the text as string """
        return self._dbConnection.get_post_text_with_id(id_)[0]
    
    def calc_score_of_post(self, text):
        print("Calculating the score of: " + text)
        return readability.getmeasures(unicode(text), lang='en')
    
    def number_db_entries(self):
        """Get Number of entries form post table"""
        return self._dbConnection.get_number_of_posts()[0]
    
    def store_rb_score(self, id_, score):
        self._dbConnection.store_readability_score(id, score)


if __name__ == "__main__":
    rdb = Readability()
