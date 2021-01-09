#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class tests the max integer function
    """

    def test_AllNumber(self):
        """ Tests to see if it finds proper max, assuming all variables are int
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([2, 1, 4, 3]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([98]), 98)

    def test_Type(self):
        """ Tests to make sure proper types are used """
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(Exception, max_integer, ["Pie", "Chocolate", "Zebr"])
        self.assertRaises(TypeError, max_integer, None)
