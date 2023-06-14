#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in a list.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int: The sum of all unique integers in the list.
    """
    unique_nums = set(my_list)
    result = sum(unique_nums)
    return result
