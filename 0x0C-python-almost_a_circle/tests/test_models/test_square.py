#!/usr/bin/python3
""" A module to test the class square"""
from models.square import Square
from models.base import Base
import json
import unittest


class TestSquare(unittest.TestCase):
    """ A class definition for test cases on class square"""
    def setUp(self):
        """ Initialising"""
        Base.reset()

    def test_attributes(self):
        """ Testing all attributes for Square"""
        s1 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(4, 4, 3, 98)
        self.assertEqual(s2.id, 98)

        s3 = Square(1, 1, 1)
        self.assertEqual(s3.id, 2)

    def test_validation(self):
        """testing validation rules"""

        with self.assertRaises(TypeError):
            s4 = Square('a', 2, 3, 5)
        with self.assertRaises(TypeError):
            s4 = Square(1, '2', 3, 5)
        with self.assertRaises(TypeError):
            s4 = Square(1, 2, '3', 5)
        with self.assertRaises(TypeError):
            s4 = Square(1, 2, '3')

        with self.assertRaises(ValueError):
            s4 = Square(-1, 3, 5)
        with self.assertRaises(ValueError):
            s4 = Square(-2, -2, 5)
        with self.assertRaises(ValueError):
            s4 = Square(0, 0, 3, 5)
        with self.assertRaises(ValueError):
            s4 = Square(1, 2, -3, 5)
        with self.assertRaises(ValueError):
            s4 = Square(1, -2, 3)
        with self.assertRaises(ValueError):
            s4 = Square(0, 0, 0, 5)

    def test_Area(self):
        """Testing for area of a rectangle"""
        s5 = Square(5)
        self.assertEqual(s5.area(), 25)
        s6 = Square(4, 4, 1)
        self.assertEqual(s6.area(), 16)

    def test_display(self):
        """Testing the output from the display"""
        s7 = Square(4)
        disp1 = "####\n####\n####\n####\n"
        self.assertEqual(s7.display(), disp1)
        s8 = Square(2, 2, 2, 2)
        disp2 = "\n\n  ##\n  ##\n"
        self.assertEqual(s8.display(), disp2)

    def test_str(self):
        """Testing the string method"""
        s9 = Square(4, 2, 1, 12)
        expected = f"[Square] ({s9.id}) {s9.x}/{s9.y} - {s9.size}"
        self.assertEqual(str(s9), expected)

    def test_update(self):
        s11 = Square(10, 10, 10, 10)
        s12 = s11.update(89)
        self.assertEqual(s11.id, 89)
        s12 = s11.update(89, 2)
        self.assertEqual(s11.size, 2)
        s12 = s11.update(89, 2, 3, 4)
        self.assertEqual(s11.x, 3)

    def to_dictionary(self):
        """Testing the to_dictionary method"""
        s13 = Square(2, 4, 1, 3, 42)
        expected_dict = {'id': 42, 'size': 2, 'x': 1, 'y': 3}
        self.assertEqual(s13.to_dictionary(), expected_dict)
        s12 = s11.update(89, 2, 3, 4)
        self.assertEqual(s11.y, 4)
