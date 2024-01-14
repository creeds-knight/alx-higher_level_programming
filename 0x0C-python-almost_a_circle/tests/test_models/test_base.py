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
    def setup(self):
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

    if __name__ == '__main__':
        unittest.main()
        Base.reset()

