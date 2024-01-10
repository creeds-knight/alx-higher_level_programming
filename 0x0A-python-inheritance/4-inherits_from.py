#!/usr/bin/python3
""" A module to check if is a subclass"""


def inherits_from(obj, a_class):
    """check if is a subclass"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
