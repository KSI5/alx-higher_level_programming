#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Get the number of keys in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to count the keys from.

    Returns:
        int: The number of keys in the dictionary.
    """
    num = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num += 1

    return num
