#!/usr/bin/python3
""" A module that converts classes to json files"""


def class_to_json(obj):
    """A returns a dictionary structure of class"""
    return obj.__dict__
