#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Prints a text with 2 new lines after each occurrence of ".", "?", and ":".

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Remove leading and trailing whitespaces
    text = text.strip()

    # Iterate over each character in the text
    for char in text:
        print(char, end="")
        if char in (".", "?", ":"):
            print("\n\n", end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
