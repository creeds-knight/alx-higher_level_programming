#!/usr/bin/python3
""" A module for Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A class for a square formed from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
