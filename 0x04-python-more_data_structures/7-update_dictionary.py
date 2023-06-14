#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to replace or add.
        value: The value to assign to the key.

    Returns:
        None
    """
    a_dictionary[key] = value
