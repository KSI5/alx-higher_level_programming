#!/usr/bin/python3

"""
Add all arguments to a Python list and save them to a file.
"""

import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a JSON file.

    Args:
        my_obj: The object to be saved.
        filename (str): The name of the file to save to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
        filename (str): The name of the file to load from.

    Returns:
        The object loaded from the JSON file.
    """
    with open(filename) as file:
        return json.load(file)


if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
