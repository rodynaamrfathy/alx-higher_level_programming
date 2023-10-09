#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None:
        my_list = []  # Create a new empty list if my_list is not provided
    for item in my_list:
            print("{}".format(item))
