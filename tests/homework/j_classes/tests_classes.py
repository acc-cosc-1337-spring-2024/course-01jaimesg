import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_die(self):
       roll = Die ()

       for _ in range(3):
        roll.roll()
        self.assertEqual(1 <= roll.get_rolled_value()<= 6, True)