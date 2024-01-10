#!/usr/bin/python3
""" A module for max of alist"""

def max_integer(list=[]):
    """ a function to return max from a lisst of ints"""
    if len(list) == 0:
        return None
    max = list[0]
    i = 1
    while i < len(list):
        if list[i] > max:
            max = list[i]
        i += 1
    return max
