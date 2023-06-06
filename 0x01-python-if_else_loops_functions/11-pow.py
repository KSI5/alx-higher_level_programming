#!/usr/bin/python3

def pow(a, b):
    """Compute a to the power of b."""
    result = 1
    for _ in range(b):
        result *= a
    return result
