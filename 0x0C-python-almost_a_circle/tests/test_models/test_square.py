#!/usr/bin/python3
"""Unittest for square"""
import unittest
import json
from models.square import Square


class TestSquare(unittest.TestCase):
    """This class tests Square methods"""
    def test_taskten(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s2 = Square(1, 2, 3, 12)
        self.assertEqual(s2.id, 12)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
