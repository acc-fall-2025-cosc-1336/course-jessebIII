import unittest


from src.examples.a_example.devprocess import multiply_numbers

class Test_Config(unittest.TestCase):

    def test_echo_value(self):
        self.assertEqual("Hello, world!", echo_value("Hello, world!"))
        self.assertEqual(5, echo_value(5))

    def test_add_numbers(self):
        self.assertEqual(5, add_numbers(2, 3))
        self.assertEqual(-1, add_numbers(2, -3))
        
        
