#!/usr/bin/python3
""" Module contains a function that returns an obj by
a JSON rep """

import json

def from_json_string(my_str):
    """ Function that returns an object by a JSON rep """

    return json.loads(my_str)
