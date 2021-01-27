#!/usr/bin/python3
"""Unittest for rectangle"""
import unittest
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This class tests rectangle"""
    def test_attributes(self):
        """Tests rectanlge attributes"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(10, 2, 1, 3, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 3)

    def test_taskthree(self):
        """Tests for int validators"""
        self.assertRaises(TypeError, Rectangle, "2", 2)
        self.assertRaises(TypeError, Rectangle, 2.5)
        self.assertRaises(TypeError, Rectangle, 2, "2")
        self.assertRaises(TypeError, Rectangle, 2, 2, "2")
        self.assertRaises(TypeError, Rectangle, 2, 2, 2, "2")
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, -1, 1)
        self.assertRaises(ValueError, Rectangle, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, -1)
        self.assertRaises(ValueError, Rectangle, 1, 1, 0, -1)
