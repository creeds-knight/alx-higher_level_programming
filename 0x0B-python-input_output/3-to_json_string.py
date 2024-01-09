#!/usr/bin/python3
""" A module for json files"""


import json


def to_json_string(my_obj):
    """ A function that returns json representation of an object string"""
    new = json.dumps(my_obj)
    return new
