#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.

    Returns:
        None
    """
    text = ""
    with open(filename, 'r') as file:
        for line in file:
            text += line.rstrip('\n')
            if search_string in line:
                text += new_string
            text += '\n'

    with open(filename, 'w') as file:
        file.write(text)
