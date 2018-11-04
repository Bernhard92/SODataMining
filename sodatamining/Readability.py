import readability
import DBConnection


class Readability:
    
    def __init__(self):
        text = ('This is an example sentence .\n'
        'Note that tokens are separated by spaces and sentences by newlines .\n')
        
        results = readability.getmeasures(unicode(text), lang='en')
        print(results['readability grades']['FleschReadingEase'])
        
        self._dbConnection = DBConnection()

    @property
    def dbConnection(self):
        return self._dbConnection
    
    def test(self):
        print("s")
        
    def get_post_from_db(self, id):
        self.dbConnection.get_post_with_id(id)
    

    def get_score_of_post(self, post):

		
        
    
