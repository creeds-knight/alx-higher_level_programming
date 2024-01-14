#!/usr/bin/python3
""" A module for the square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialisation of class square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A method to print out a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Getting the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ A method to update square"""
        attrs = ['id', 'size', 'x', 'y']
        for attr, value in zip(attrs, args):
            setattr(self, attr, value)
        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def to_dictionary(self):
        """ A method for dictionary representation"""
        dct = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dct
