#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    def height(self):
        return self.__height

    def height(self):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    def area(self):
        return self.__width * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({},{})".format(self.__width, self.__height)
