#!/usr/bin/python3
"""class that defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """private instance attributes
        with leading double underscore"""
        self.__width = width
        self.__height = height

    """property to retrieve width"""
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """function defining private property"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """function defining private property"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        return f"{{'_Rectangle__height': {self.__height}, '_Rectangle__width': {self.__width}}}"
