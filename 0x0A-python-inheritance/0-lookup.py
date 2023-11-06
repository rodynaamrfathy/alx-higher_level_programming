#!/usr/bin/python3
""" a function that returns the list of
available attributes and methods of an object"""


def lookup(obj):
    """
    Looks up object attributes and methods.
    Args:
        obj (object): the object to list.
    Return:
    List: the list of attributes.
    """
    return (dir(obj))
