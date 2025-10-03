import sys, os
import unittest

# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from tests.homework.d_repetition import tests_repetition


# Load and run tests from tests_repetition
suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner().run(suite)
