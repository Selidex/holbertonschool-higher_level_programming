#!/usr/bin/python3
"""Unittest for base"""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """This class tests Base"""


    def test_taskone(self):
        """tests task one functiosn"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
        b5 = Base(-1)
        self.assertEqual(b5.id, -1)
        b6 = Base(None)
        self.assertEqual(b6.id, 3)
