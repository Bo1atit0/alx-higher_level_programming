#!/usr/bin/python3
"""
Text Indentation module
Prototype: def text_indentation(text):
Raises:
  exceptions if text is not a string.
"""


def text_indentation(text):
    """
    A text indentation Function that
    prints 2 new lines after these chars:
    ".", "?" and ":"
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    # variable for final string
    result_str = ''

    # flag for spaces at the beginning of newline
    start_of_line = True

    for char in text:

        if char in ['.', '?', ':']:
            result_str += char + '\n\n'
            start_of_line = True
        elif not start_of_line or char != " ":
            result_str += char + ''
            start_of_line = False
    print(result_str, end='')
