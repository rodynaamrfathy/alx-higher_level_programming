#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    value = int(value)
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        sys.stderr.write("Exception: Unknown format code 'd' for object of type {}'".format(value) + \n)
        return False
