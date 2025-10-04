import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
import unittest
from homework.c_decisions.decisions import get_letter_grade

class TestLetterGrade(unittest.TestCase):
    def Test_A_grade(self):
        self.assertEqual(get_letter_grade(95), 'A')
        self.assertEqual(get_letter_grade(90), 'A')
        self.assertEqual(get_letter_grade(100), 'A')

    def Test_B_grade(self):
        self.assertEqual(get_letter_grade(85), 'B')
        self.assertEqual(get_letter_grade(80), 'B')
        self.assertEqual(get_letter_grade(89), 'B')
    
    def Test_C_grade(self):
        self.assertEqual(get_letter_grade(75), 'C')
        self.assertEqual(get_letter_grade(70), 'C')
        self.assertEqual(get_letter_grade(79), 'C')

    def Test_D_grade(self):
        self.assertEqual(get_letter_grade(65), 'D')
        self.assertEqual(get_letter_grade(60), 'D')
        self.assertEqual(get_letter_grade(69), 'D')

    def Test_F_grade(self):
        self.assertEqual(get_letter_grade(50), 'F')
        self.assertEqual(get_letter_grade(0), 'F')
        self.assertEqual(get_letter_grade(59), 'F')

if __name__ == '__main__':
    unittest.main()
