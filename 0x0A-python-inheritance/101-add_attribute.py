#!/usr/bin/python3
"""Adds a new attribute to an object if it’s possible """

def add_attribute(obj, attribute, value):
    """Adds a new attribute"""

    if not hasattr(obj, attr):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
