#!/usr/bin/python3
""" Test module for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase(unittest.TestCase):
    """ Test class for base"""
    def setUp(self):
        """ Sets all back to 0 instances of base"""
        Base.reset()

    def test_id(self):
        case1 = Base()
        self.assertEqual(case1.id, 1)
        case2 = Base()
        self.assertEqual(case2.id, 2)
        case3 = Base()
        self.assertEqual(case3.id, 3)
        case4 = Base(12)
        self.assertEqual(case4.id, 12)
        case5 = Base()
        self.assertEqual(case5.id, 4)

    def test_to_json_string(self):
        """ Testing conversion of a dictionary to json string"""
        lst_dct = [{'id':3, 'width': 6, 'height': 8}, {'id': 98, 'size': 2}]
        expected = '[{"id": 3, "width": 6, "height": 8}, {"id": 98, "size": 2}]'
        self.assertEqual(Base.to_json_string(lst_dct), expected)

