#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Print contents of a UTF8 text file to stdout. """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
