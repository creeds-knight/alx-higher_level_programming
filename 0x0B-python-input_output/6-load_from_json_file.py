#!/usr/bin/python3
""" A module for loading json objcts from files"""


import json


def load_from_json_file(filename):
    """ A function to load json objects from files"""
    with open(filename, 'r') as f:
        x = json.load(f)
        return x
