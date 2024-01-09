#!/usr/bin/python3
""" A module that appends data to a file"""


def append_write(filename="", text=""):
    """ A function to append data to a text file"""
    with open(filename, 'a+', encoding='utf-8') as f:
        current_position = f.tell()
        f.write(text)
        final_position = f.tell()
        return (final_position - current_position)
