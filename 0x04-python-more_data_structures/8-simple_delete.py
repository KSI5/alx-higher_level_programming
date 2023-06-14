#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete a key from a dictionary.

    Args:
        a_dictionary (dict): The dictionary to modify.
        key (str): The key to delete.

    Returns:
        None
    """
    a_dictionary.pop(key, None)
