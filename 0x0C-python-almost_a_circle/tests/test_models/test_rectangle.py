#!/usr/bin/python3
""" A module to test rectangle"""
import json
import os
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """ Tests for class Rectangle"""
    def setUp(self):
        """ Initialing """
        Base.reset()

    def test_attributes(self):
        r1 = Rectangle(1, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 4, 4, 2, 98)
        self.assertEqual(r2.id, 98)

        r3 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r3.id, 2)

    def test_validation(self):
        """ testing validation rules"""
        with self.assertRaises(TypeError):
            r4 = Rectangle('a', 2, 3, 5)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, '2', 3, 5)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, '3', 5)
        with self.assertRaises(TypeError):
            r4 = Rectangle(1, 2, 3, '5')
        with self.assertRaises(ValueError):
            r4 = Rectangle(-1, 2, 3, 5)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, -2, 3, 5)
        with self.assertRaises(ValueError):
            r4 = Rectangle(0, 2, 3, 5)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, -3, 5)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -5)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 0, 3, 5)

    def test_Area(self):
        """ Testing for area of a rectangle)"""
        r5 = Rectangle(5, 4)
        self.assertEqual(r5.area(), 20)
        r6 = Rectangle(4, 8)
        self.assertEqual(r6.area(), 32)

    def test_display(self):
        """ Testing the output from the display"""
        r7 = Rectangle(2, 4)
        disp1 = "##\n##\n##\n##\n"
        self.assertEqual(r7.display(), disp1)
        r8 = Rectangle(2, 4, 2, 2)
        disp2 = "\n\n  ##\n  ##\n  ##\n  ##\n"
        self.assertEqual(r8.display(), disp2)

    def test_str(self):
        """ Testing the string method"""
        r9 = Rectangle(4, 6, 2, 1, 12)
        w = r9.width
        h = r9.height
        expected = f"[Rectangle] ({r9.id}) {r9.x}/{r9.y} - {w}/{h}"
        self.assertEqual(str(r9), expected)

    def test_update(self):
        r11 = Rectangle(10, 10, 10, 10)
        r12 = r11.update(89)
        self.assertEqual(r11.id, 89)
        r12 = r11.update(89, 2)
        self.assertEqual(r11.width, 2)
        r12 = r11.update(89, 2, 3)
        self.assertEqual(r11.height, 3)
        r12 = r11.update(89, 2, 3, 4)
        self.assertEqual(r11.x, 4)
        r12 = r11.update(89, 2, 3, 4, 5)
        self.assertEqual(r11.y, 5)

    def test_to_dictionary(self):
        """Testing the to_dictionary method"""
        r13 = Rectangle(2, 4, 1, 3, 42)
        expected_dict = {'id': 42, 'width': 2, 'height': 4, 'x': 1, 'y': 3}
        self.assertEqual(r13.to_dictionary(), expected_dict)
