#!/usr/bin/python3
""" Module that contains a function that writes to a text file
"""

def write_file(filename="", text=""):
    """ Function that writes to a text file """

    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
