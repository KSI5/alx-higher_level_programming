#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Get the elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing elements present in only one of the sets.
    """
    diff_set = set_1.symmetric_difference(set_2)
    return diff_set
