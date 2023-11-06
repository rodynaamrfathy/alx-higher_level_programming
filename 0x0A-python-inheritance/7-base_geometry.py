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

