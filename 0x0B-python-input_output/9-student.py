#!/usr/bin/python3
""" A module for student"""


class Student:
    """ A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A dictionary of student"""
        return self.__dict__
