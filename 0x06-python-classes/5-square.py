#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square that sets a private size for the square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Check if the size is true to specifications."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
        """
        if size = 0:
            print()
            return None

        for row in range(0, size):
            for column in range(0, size):
                print('#', end='')
            print()
