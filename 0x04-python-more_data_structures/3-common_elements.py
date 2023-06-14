#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Get the common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing the common elements between set_1 and set_2.
    """
    common_set = set_1.intersection(set_2)
    return common_set
