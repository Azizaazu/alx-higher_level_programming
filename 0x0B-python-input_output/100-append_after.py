#!/usr/bin/python3
""" Module that executes a function that appends a line """

def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found """

    new_lines = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string + "\n")
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
