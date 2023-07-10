#!/usr/bin/python3

"""
Module: 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.
    Returns True if it is, False otherwise.
    """
    return type(obj) is a_class
