import unittest

from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio


class Test_Config(unittest.TestCase):
            
            
    def test_get_option_ration(self):
        self.assertEqual(get_options_ratio(5, 20), .25)
        self.assertEqual(get_options_ratio(10, 20), .5)

    def test_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating (.91), "Excellent")
        self.assertEqual(get_faculty_rating (.85), "Very Good")
        self.assertEqual(get_faculty_rating (.71), "Good")
        self.assertEqual(get_faculty_rating (.66), "Needs Improvements")
        self.assertEqual(get_faculty_rating (.50), "Unacceptable")
       



