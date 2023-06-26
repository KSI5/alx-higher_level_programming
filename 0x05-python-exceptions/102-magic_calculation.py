#!/usr/bin/python3

import sys


def safe_print_division(a, b):
    """Divide two integers and print the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division.
            Returns None if a zero division error
            occurs or any other exception happens.
    """
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))
        return result
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
        return None
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
