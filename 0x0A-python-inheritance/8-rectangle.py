#!/usr/bin/python3
""" define a class BaseGeometry"""


class BaseGeometry:
    """Class with public instance methods"""

    def area(self):
        """ raises an Exception with the message area() """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name (string): name
            value (int): value
        """

        self.name = name
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Represents a rectangle
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Initializes an instance

        Args:
            - width: rectangle width
            - height: rectangle height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
