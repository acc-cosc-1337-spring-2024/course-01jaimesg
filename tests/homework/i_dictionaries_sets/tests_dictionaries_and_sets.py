import unittest

#from src.homework.i_dictionaries_sets.sets import add_inventory, delete_inventory


class Test_Config(unittest.TestCase):


    def test_get_students_who_took_prog1_and_prog2(self):
        prog1 = set(['Student1', 'Student2', 'Student3'])
        prog2 = set(['Student3', 'Student4', 'Student5'])
        union_set = prog1.intersection(prog2)
        expected_set = set(['Student3'])

    def test_get_students_who_took_only_prog2(self):
        prog1 = set(['Student1', 'Student2', 'Student3'])
        prog2 = set(['Student3', 'Student4', 'Student5'])
        union_set = (prog2)
        expected_set = set(['Student1', 'Student2', 'Student3'])
        
    def test_get_students_who_took_prog1_not_prog2(self):
        prog1 = set(['Student1', 'Student2', 'Student3'])
        prog2 = set(['Student3', 'Student4', 'Student5'])
        union_set = prog1.difference(prog2)
        expected_set = set(['Student1', 'Student2'])
    
    def test_get_students_who_took_prog2_not_prog1(self):
        prog1 = set(['Student1', 'Student2', 'Student3'])
        prog2 = set(['Student3', 'Student4', 'Student5'])
        union_set = prog2.difference(prog1)
        expected_set = set(['Student4', 'Student5'])



 