import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
import unittest
from src.homework.d_repetition.repetition import get_factorial

from src.homework.d_repetition.repetition import sum_odd_numbers



class Test_Config(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEqual(get_factorial(5), 120)
        self.assertEqual(get_factorial(1), 1)
        self.assertEqual(get_factorial(0), 1)

    def test_sum_odd_numbers(self):
        self.assertEqual(sum_odd_numbers(5), 9)
        self.assertEqual(sum_odd_numbers(1), 1)
