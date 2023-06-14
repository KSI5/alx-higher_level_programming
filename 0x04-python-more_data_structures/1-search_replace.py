#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element with another element in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element to replace with.

    Returns:
        list: A new list where all occurrences of the search element are replaced.
    """
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
