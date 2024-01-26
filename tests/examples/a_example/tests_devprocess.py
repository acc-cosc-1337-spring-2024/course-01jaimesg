import unittest

from src.examples.a_example.devprocess import add_numbers

class Test_Config(unittest.TestCase):

    def test_add_numbers_2(self): #create one test function-task=test that add numbers work as expected
        self.assertEqual(2, add_numbers(1, 1))

def test_substract_numbers_1(self):
    self.assertEqual(5, subtract_numbers(10,5))
    
