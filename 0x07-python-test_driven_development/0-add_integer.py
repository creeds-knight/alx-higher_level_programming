#!/usr/bin/python3
"""
    A module that contains a function that adds 2 integers
"""

def add_integer(a, b=98):
    """
        A function that adds two intgers or floats
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except (OverflowError, ValueError):
        pass
    try:
        b = int(b)
    except (OverflowError, ValueError):
        pass

    return (a + b)

