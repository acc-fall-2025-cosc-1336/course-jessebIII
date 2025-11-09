"""List utility functions for homework.

Do not use built-in min()/max() for the implementations below; use loops.
"""

def get_lowest_list_value(values):
	"""Return the lowest value in the list `values` using a loop.

	Raises ValueError if the list is empty.
	"""
	if values is None or len(values) == 0:
		raise ValueError("values must be a non-empty list")

	lowest = values[0]
	i = 1
	while i < len(values):
		if values[i] < lowest:
			lowest = values[i]
		i += 1

	return lowest
