import unittest

from src.examples.b_input_proc_output.input_process_output import add_values, test_config, floating_point_division

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_numbers(self):
        self.assertEqual(add_values(3, 4), 7)


def test_floating_point_division_1(self):
    self.assertEqual(floating_point_division(5, 2), 2.5)

def test_floating_point_division_2(self):
    self.assertEqual(floating_point_division(20, 10), 2)