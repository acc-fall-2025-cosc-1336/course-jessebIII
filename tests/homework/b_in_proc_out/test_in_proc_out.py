import sys, os
import unittest

# Add project root to sys.path so Python can find src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from src.homework.b_in_proc_out.output import get_number, get_sales_tax_amount, get_tip_amount

class Test_AllFunctions(unittest.TestCase):

    # ===== get_number tests =====
    def test_get_number_1(self):
        self.assertEqual(get_number(1), 1)

    def test_get_number_2(self):
        self.assertEqual(get_number(2), 2)

    # ===== get_sales_tax_amount tests =====
    def test_sales_tax_normal(self):
        # Normal meal amount
        self.assertAlmostEqual(get_sales_tax_amount(20), 1.35, places=2)

    def test_sales_tax_zero(self):
        # Meal amount 0
        self.assertAlmostEqual(get_sales_tax_amount(0), 0.00, places=2)

    def test_sales_tax_large(self):
        # Large meal amount
        self.assertAlmostEqual(get_sales_tax_amount(1000), 67.50, places=2)

    # ===== get_tip_amount tests =====
    def test_tip_normal(self):
        # Flat tip $3
        self.assertEqual(get_tip_amount(3), 3.00)

    def test_tip_zero(self):
        self.assertEqual(get_tip_amount(0), 0.00)

    def test_tip_large(self):
        self.assertEqual(get_tip_amount(100), 100.00)

