#!/usr/bin/python3
""" returns True if the object is exactly an instance
of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """
    Function to determine if obj is an instance of a class
    Args:
        - obj: object to look at
        - a_class: class to verify the instanceof

    Return:
        True if the object is exactly an instance
        otherwise False
    """

    if type(obj) is a_class:
        return True
    return False
