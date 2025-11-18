
def get_lowest_list_value(values):
	if values is None or len(values) == 0:
		raise ValueError("values must be a non-empty list")

	lowest = values[0]
	i = 1
	while i < len(values):
		if values[i] < lowest:
			lowest = values[i]
		i += 1

	return lowest


def get_highest_list_value(values):
    if values is None or len(values) == 0:
        raise ValueError("values must be a non-empty list")

    highest = values[0]
    i = 1
    while i < len(values):
        if values[i] > highest:
            highest = values[i]
        i += 1

    return highest


def get_p_distance(list1, list2):
	"""Return the p-distance (proportion of differing positions) between two lists.

	Both lists must be non-empty and have the same length.
	"""
	if list1 is None or list2 is None:
		raise ValueError("inputs must be non-empty lists of equal length")
	if len(list1) == 0 or len(list2) == 0:
		raise ValueError("inputs must be non-empty lists of equal length")
	if len(list1) != len(list2):
		raise ValueError("inputs must be lists of the same length")

	diffs = 0
	i = 0
	while i < len(list1):
		if list1[i] != list2[i]:
			diffs += 1
		i += 1

	return diffs / len(list1)


def get_p_distance_matrix(list1):
	"""Return the p-distance matrix for a list of equal-length lists/strings.

	The result is an n x n matrix where element [i][j] is the p-distance
	between list1[i] and list1[j]. Uses `get_p_distance` for each pair.
	"""
	if list1 is None:
		raise ValueError("input must be a non-empty list of sequences")
	n = len(list1)
	if n == 0:
		return []

	# initialize matrix with zeros
	p_distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]

	i = 0
	while i < n:
		j = 0
		while j < n:
			if i == j:
				p_distance_matrix[i][j] = 0.0
			else:
				p_distance_matrix[i][j] = get_p_distance(list1[i], list1[j])
			j += 1
		i += 1

	return p_distance_matrix
