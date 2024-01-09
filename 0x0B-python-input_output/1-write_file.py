#!/usr/bin/python3
""" A Module to write to a file"""


def write_file(filename="", text=""):
    """ A function to write a string of text to a file in utf-8"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
