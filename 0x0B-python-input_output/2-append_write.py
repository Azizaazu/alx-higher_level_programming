#!/usr/bin/python3
""" Module contains a function that appends to a text file """

def append_write(filename="", text=""):
     """ Function that appends to a text file
     """
     with open(filename, "a", encoding="utf-8") as file:
         num_chars_added = file.write(text)
     return num_chars_added
