import unittest
from app.models import Votes

class VotesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Votes class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_votes = Votes()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_votes,Votes))
        
        
        