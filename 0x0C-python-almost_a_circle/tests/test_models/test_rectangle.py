#!/usr/bin/python3
"""Unittest for rectangle"""
import unittest
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class tests rectangle"""
    def test_tasktwo(self):
        """Tests task two functions"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 3)
        r3 = Rectangle(11, 2)
        self.assertEqual(r3.id, 2)
