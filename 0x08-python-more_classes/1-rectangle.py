#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a Rectangle."""
    
    def __init__(self, width=0, height=0):
        """intialize a new rectangle

        args:
            width (int): the width of new rectangle
            height (int): th height if the new rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """returns the value of the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the rectangle width and check if it is correct"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        else if width < 0:
            raise TypeError("width must be >= 0")
        self.__width =  value

    @property
    def height(self):
        """returns the value of the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the rectangle height and check if it is correct"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        else if height < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
