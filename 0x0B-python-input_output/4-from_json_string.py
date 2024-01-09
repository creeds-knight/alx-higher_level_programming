#!/usr/bin/python3
""" A module de deserialize a string"""

import json


def from_json_string(my_str):
    """ A function to deserialize a string"""
    new = json.loads(my_str)
    return new
