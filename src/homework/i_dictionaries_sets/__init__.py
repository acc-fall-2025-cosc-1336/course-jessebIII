def get_p_distance(list1, list2):
    if list1 is None or list2 is None:
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

from .dictionary import add_inventory, remove_inventory_widget
