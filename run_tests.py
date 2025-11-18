import sys
import os
import unittest

# Ensure repository root is on sys.path so `src` and `tests` packages import correctly.
repo_root = os.path.abspath(os.path.dirname(__file__))
if repo_root not in sys.path:
	sys.path.insert(0, repo_root)

# Import the specific test module and run it.
from tests.homework.g_lists_and_tuples import test_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(test_lists_and_tuples)
unittest.TextTestRunner().run(suite)
