#!/usr/bin/python3
""" A mdule for base class used to track the id """
import json
import os
import csv
import turtle


class Base:
    """
    A class definition for tracking of the ids
    using base.py
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialisation for the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method to return json representation of a dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A method to save to a file"""
        file_name = f"{cls.__name__}.json"
        if list_objs is None or len(list_objs) == 0:
            string = Base.to_json_string([])
        else:
            new_lst = []
            for obj in list_objs:
                new_lst.append(obj.to_dictionary())
            string = Base.to_json_string(new_lst)

        with open(file_name, 'w') as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list representation of a json string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to instance"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return None
        if len(dictionary) == 0:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loading from file"""
        file_name = f"{cls.__name__}.json"
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r') as f:
            lst = Base.from_json_string(f.read())
        new_lst = lst()
        for i in lst:
            new_lst.append(cls.create(**i))
        return new_lst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saving to a csv file"""
        file_name = f"{cls.__name__}.csv"
        shp = cls.__name__
        dct = {
                'Square': ['id', 'size', 'x', 'y'],
                'Rectangle': ['id', 'width', 'height', 'x', 'y']
                }
        header = ','.join(dct[shp]) + '\n'
        rows = [','.join(map(str, [getattr(obj, attr, '') for attr in
                dct[shp]])) for obj in list_obj] if list_objs else []

        with open(file_name, 'w', newline='') as f:
            f.write(header + '\n'.join(rows))

    @classmethod
    def load_from_file_csv(cls):
        file_name = f"{cls.__name__}.csv"
        shp = cls.__name__
        dct = {
                'Square': ['id', 'size', 'x', 'y'],
                'Rectangle': ['id', 'width', 'height', 'x', 'y']
                }
        objects = []

        with open(file_name, 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                obj_args = {attr: int(row[attr]) for attr in dct[shape] if
                            row[attr].isdigit()}
                obj = cls(**obj_args)
                objects .append(obj)
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """drawing the shapes"""
        window = turtle.Screen()
        window.bgcolor("black")

        pen = turtle.Turtle()
        pen.speed(2)

        for rectangle in list_rectangles:
            width = rectangle.width
            height = rectangle.height
            x = rectangle.x
            y = rectangle.y
            color = "red"

            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(color)
            for i in range(2):
                pen.forward(width)
                pen.left(90)
                pen.forward(height)
                pen.left(90)

        for square in list_squares:
            size = square.size
            x = square.x
            y = square.y
            color = "yellow"

            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(color)
            for i in range(4):
                pen.forwad(side)
                pen.left(90)
        turtle.done()

    @classmethod
    def reset(cls):
        """instances will be reinitiallised to 0"""
        Base.__nb_objects = 0
