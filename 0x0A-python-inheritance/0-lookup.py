#!/usr/bin/python3

"""Function that returns list of available attributes"""


def lookup(obj):
    """returns list or methods in an object"""
    return dir(obj)
