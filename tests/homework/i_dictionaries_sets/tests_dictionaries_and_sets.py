import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, delete_inventory


class Test_Config(unittest.TestCase):


    def test_add_inventory(self):
        Inventory = {}
        
        add_inventory(Inventory, 'Widget1', 10)
        self.assertEqual(Inventory['Widget1'], 10)
        add_inventory(Inventory, 'Widget1', 25)
        self.assertEqual(Inventory['Widget1'], 35)

    def test_delete_inventory(self):
        add_inventory(Inventory, 'Widget2', 50)
        delete_inventory(Inventory, 'Widget1')
        self.assertEqual(len(Inventory))

 