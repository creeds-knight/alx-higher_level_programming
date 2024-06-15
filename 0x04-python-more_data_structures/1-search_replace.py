#!/usr/bin/python3
""" replaces all occurances of an element by another in a new_list"""


def search_replace(my_list, search, replace):
    new_lst = [replace if elm == search else elm for elm in my_list]
    return new_lst
