#!/usr/bin/python3

""" Prints 2 new lines after ".?:" characters """

def text_indentation(text):
    """ Prints 2 new lines after ".?:" characters

    Args:
        text: string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    t = text[:]

    for i in ".?:":
        list_text = s.split(i)
        t = ""
        for j in list_text:
            j = j.strip(" ")
            t = j + i if t is "" else t + "\n\n" + j + i

    print(t[:-3], end="")
