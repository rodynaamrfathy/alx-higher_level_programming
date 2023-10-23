#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        value_as_int = int(value)
        print("{:d}".format(value_as_int))
        return True
    except (ValueError, TypeError):
        sys.stderr.write("Exception: Unknown format code 'd' for object of type '{}'\n".format(value.__class__.__name__))
        return False
