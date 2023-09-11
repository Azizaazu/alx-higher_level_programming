#!/usr/bin/python3
""" class MyInt inherits from int"""

class MyInt(int):
    """ Class int """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
