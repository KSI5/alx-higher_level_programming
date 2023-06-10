#!/usr/bin/python3

def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first char."""
    if len(sentence) == 0:
        first_character = None
    else:
        first_character = sentence[0]
    return len(sentence), first_character
