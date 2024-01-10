#!/usr/bin/python3
""" A module for searching and updating"""


def append_after(filename="", search_string="", new_string=""):
    """ A function to search and insert a new string"""
    if len(search_string) == 0:
        return
    string = str()
    with open(filename, 'r') as f:
        while (line := f.readline()):
            string += line
            if search_string in line:
                string += new_string

    with open(filename, 'w') as f:
        f.writelines(string)
