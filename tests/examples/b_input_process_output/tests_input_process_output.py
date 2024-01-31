import unittest

from src.examples.b_input_proc_output.input_process_output import add_values, get_remainder, operator_precedence_1, test_config, floating_point_division, integer_division, power_function

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_add_numbers(self):
        self.assertEqual(add_values(3, 4), 7)


    def test_floating_point_division_1(self):
          self.assertEqual(floating_point_division(5, 2), 2.5)

    def test_floating_point_division_2(self):
        self.assertEqual(floating_point_division(20, 8), 2.5)

    def test_integer_division_1(self):
        self.assertEqual(integer_division(20, 8), 2)

    def test_operator_precedence_1(self):
        self.assertEqual(operator_precedence_1(12, 6, 3), 6)

    def test_operator_precedence_2(self):
        self.assertEqual(operator_precedence_1(12, 6, 3), 6)


    def test_power_function(self):
        self.assertEqual(power_function(2, 2), 4)
        self.assertEqual(power_function(8, 2), 64)

    def test_power_function_cubed(self):
        self.assertEqual(power_function(2, 3), 8)
    
    def test_get_remainder(self):
        self.assertEqual(get_remainder(2, 2), 0)

