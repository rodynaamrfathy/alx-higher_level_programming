#!/usr/bin/python3
"""a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    file: file to be opened.
    text: to be appended
    returns: the number of characters added"""

    with open(filename, "a", encoding="utf-8") as f:
        content = f.write(text)
        return content
