import sys, os
import unittest

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from tests.homework.e_functions import tests_functions

# Load and run tests from tests_repetition
suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner().run(suite)
