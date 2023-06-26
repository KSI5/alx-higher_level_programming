#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Execute a function safely and handle exceptions.

    Args:
        fct (function): The function to execute.
        *args: Variable-length argument list for the function.

    Returns:
        The result of the function if it executes successfully,
        None if an exception occurs during execution.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
