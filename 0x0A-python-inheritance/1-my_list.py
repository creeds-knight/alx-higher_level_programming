#!/usr/bin/python3
""" A module to print sorted lists"""


class MyList(list):
    """ A class that inherits from list"""

    def print_sorted(self):
        """ A function to print sorted list"""
        new_ls = sorted(self)
        print(new_ls)
