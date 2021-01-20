#!/usr/bin/python3
"""Int inherited class goes here"""


class MyInt(int):
    """My own int class"""
    def __eq__(self, other):
        """flips the eq method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """flips the ne method"""
        return super().__eq__(other)
