#!/usr/bin/python3
""" using unnittest"""
import unittest
maxi = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing the function"""

    def test_max_integer(self):
        """method to test"""
        #case1
        self.assertEqual(maxi([1,2,3]), 3)

        #case2
        self.assertEqual(maxi())
        self.assertIsNone(maxi([]))

        #case3
        self.assertEqual(maxi([90]),90)

        #case4
        self.assertEqual(maxi([80,10,13]), 80)
