#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square that sets a private size for the square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
            return None
        
        [print("") for i in range(0, self.__position[1])]
        for row in range(0, self.__size):
            for space in range(0, self.__position[0]):
                print(' ', end='')
            for column in range(0, self.__size):
                print('#', end='')
            print()
