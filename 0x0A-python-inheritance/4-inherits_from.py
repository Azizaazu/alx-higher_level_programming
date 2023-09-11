#!/usr/bin/python3
""" Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False """

def inherits_from(obj, a_class):
    """ returns True if the object is an instance """
    if isinstance(obj, a_class):
        return True
    if type(obj) == type:
        return False
    return inherits_from(obj.__class__, a_class)
