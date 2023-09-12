#!/usr/bin/python3

""" Returns List of available attributes and methods of an object """

def lookup(obj):
    """Returns list of available attributes"""
    return dir(obj)
