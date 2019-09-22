import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Category class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_category = Category()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))
        
        
        