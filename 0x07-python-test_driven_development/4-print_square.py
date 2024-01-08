#!/usr/bin/python3
""" A module to print a square"""


def print_square(size):
    """ A function to print a square using #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
