#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the value of the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the rectangle width
            and checks if it is correct."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the rectangle height
            and checks if it is correct."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        return (2 * self.__width) + (2 * self.__height)
