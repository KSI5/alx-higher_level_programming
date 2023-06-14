#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    Create a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The dictionary to process.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    new_dict = a_dictionary.copy()
    keys = list(new_dict.keys())
    for key in keys:
        new_dict[key] *= 2
    return new_dict
