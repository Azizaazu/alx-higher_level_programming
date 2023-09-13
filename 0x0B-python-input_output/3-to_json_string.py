#!/usr/bin/python3
""" Module contains a function that returns the JSON
"""
import json

def to_json_string(my_obj):
    """ Function that returns the JSON rep of an object """

    return json.dumps(my_obj)
