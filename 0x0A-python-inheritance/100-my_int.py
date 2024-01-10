#!/usr/bin/python3
""" A module for inheritance from integer"""


class MyInt(int):
    """ A class to inherit from int"""
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
