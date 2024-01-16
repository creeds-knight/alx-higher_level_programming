#!/usr/bin/python3
""" A module for class rectangle"""
from models.base import Base


class Rectangle(Base):
    """ A definition of   Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialisation of class rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ A method to return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ A method to print out the rectangle with char#"""
        char = "#"
        res = ""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x)
            print(char * self.__width, end="")
        print()

    def __str__(self):
        """ Print the rectangle"""
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """ update attributes with both no-keyword and keyword"""
        attrs = ['id', 'width', 'height', 'x', 'y']

        for attr, value in zip(attrs, args):
            setattr(self, attr, value)
        for key, value in kwargs.items():
            if key in attrs:
                setattr(self, key, value)

    def to_dictionary(self):
        """ A method to return a dictionary rectangle"""
        dct = {"id": self.id, "width": self.width, "height": self.height,
               "x": self.x, "y": self.y}
        return dct
