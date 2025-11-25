import os
import sys
import unittest

# allow importing `src` when running this test file directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from src.homework.i_dictionaries_sets import get_p_distance
from src.homework.i_dictionaries_sets import get_p_distance


def test_imported_callable():
	assert callable(get_p_distance)


class Test_Config(unittest.TestCase):

	def test_add_inventory(self):
		from src.homework.i_dictionaries_sets import add_inventory, remove_inventory_widget

		inv = {}
		add_inventory(inv, 'widgetA', 5)
		self.assertIn('widgetA', inv)
		self.assertEqual(inv['widgetA'], 5)

		add_inventory(inv, 'widgetA', 3)
		self.assertEqual(inv['widgetA'], 8)

		# remove and verify returned quantity
		removed = remove_inventory_widget(inv, 'widgetA')
		self.assertEqual(removed, 8)
		self.assertNotIn('widgetA', inv)

		# additional assertion: adding Widget1 with quantity 10
		inventory_dictionary = {}
		add_inventory(inventory_dictionary, 'Widget1', 10)
		self.assertIn('Widget1', inventory_dictionary)
		self.assertEqual(inventory_dictionary['Widget1'], 10)

		# add 25 more to Widget1 and verify updated total is 35
		add_inventory(inventory_dictionary, 'Widget1', 25)
		self.assertEqual(inventory_dictionary['Widget1'], 35)

		# adding -10 should decrease the quantity to 25
		add_inventory(inventory_dictionary, 'Widget1', -10)
		self.assertEqual(inventory_dictionary['Widget1'], 25)

	def test_remove_inventory_widget(self):
		from src.homework.i_dictionaries_sets import add_inventory, remove_inventory_widget

		inv = {}
		add_inventory(inv, 'widget1', 7)
		add_inventory(inv, 'widget2', 12)

		removed = remove_inventory_widget(inv, 'widget1')
		# after removal, only widget2 should remain
		self.assertEqual(len(inv), 1)
		self.assertIn('widget2', inv)
		self.assertEqual(inv['widget2'], 12)

