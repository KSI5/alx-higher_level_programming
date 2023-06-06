#!/usr/bin/python3

def print_last_digit(number):
    """Will print the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
