#!/usr/bin/python3
def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return add(a, b) + sum(range(4, 6))
    else:
        return sub(a, b)
