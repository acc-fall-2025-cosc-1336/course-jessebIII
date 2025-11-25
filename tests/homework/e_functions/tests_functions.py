import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src')))
import unittest
from homework.e_functions.value_return_functions import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):

    def test_get_gross_pay(self):
        self.assertAlmostEqual(get_gross_pay(40, 20), 800)
        self.assertAlmostEqual(get_gross_pay(45, 20), 950)
        self.assertAlmostEqual(get_gross_pay(0, 20), 0)

    def test_get_fica_tax(self):
        self.assertAlmostEqual(get_fica_tax(1000), 76.5)
        self.assertAlmostEqual(get_fica_tax(0), 0)

    def test_get_federal_tax(self):
        self.assertAlmostEqual(get_federal_tax(1000), 80)
        self.assertAlmostEqual(get_federal_tax(0), 0)

    # def test_get_net_pay(self):
    #     gross_pay = 1000
    #     fica = get_fica_tax(gross_pay)
    #     federal_tax = get_federal_tax(gross_pay)
    #     expected_net_pay = gross_pay - fica - federal_tax
    #     self.assertAlmostEqual(get_net_pay(gross_pay, fica, federal_tax), expected_net_pay)