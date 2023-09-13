#!/usr/bin/python3
""" Module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""

def class_to_json(obj):
    """ Function returns the dictionary description of an obj """

    if not isinstance(obj, type(None)):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        elif hasattr(obj, "__iter__"):
            return [class_to_json(item) for item in obj]
        elif isinstance(obj, (str, int, bool)):
            return obj
    return None
