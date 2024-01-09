#!/usr/bin/python3
""" A module to json to files"""


import json


def save_to_json_file(my_obj, filename):
    """ A function to save an object to afile"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
