#!/usr/bin/python3

"""function that return true if object is instance"""


def inherits_from(obj, a_class):
    """child class"""
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return true
    else:
        return False

