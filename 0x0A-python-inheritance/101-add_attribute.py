#!/usr/bin/python3
""" A module for attribute addition"""


def add_attribute(cls, attrib, value):
    """ adds attrr if posible """
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, attrib, value)
