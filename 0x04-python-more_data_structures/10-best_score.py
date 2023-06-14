#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in the dictionary.

    Args:
        a_dictionary (dict): The dictionary to process.

    Returns:
        str: The key with the biggest integer value.
             If no score is found, returns None.
    """
    if not a_dictionary:
        return None

    return max(a_dictionary, key=a_dictionary.get)
