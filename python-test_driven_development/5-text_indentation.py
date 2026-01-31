#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: String to print with indentation

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")

        # If we hit a delimiter, print 2 newlines and skip following spaces
        if text[i] in '.?:':
            print('\n')
            i += 1
            # Skip any spaces after the delimiter
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
