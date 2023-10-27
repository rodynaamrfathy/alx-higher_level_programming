#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """Represents a square. that sets a private size for the square"""
    def __init__(self, size):

        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """

        self.__size = size
