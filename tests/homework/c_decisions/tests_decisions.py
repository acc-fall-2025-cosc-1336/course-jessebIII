import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
import unittest
from homework.c_decisions.decisions import get_letter_grade

class TestLetterGrade(unittest.TestCase):

    def test_table3_cases(self):
        self.assertEqual(get_letter_grade(95), 'A')
        self.assertEqual(get_letter_grade(85), 'B')
        self.assertEqual(get_letter_grade(75), 'C')
        self.assertEqual(get_letter_grade(65), 'D')
        self.assertEqual(get_letter_grade(50), 'F')

if __name__ == '__main__':
    unittest.main()
