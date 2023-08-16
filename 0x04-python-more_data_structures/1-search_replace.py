#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for index, n in enumerate(new_list):
        if n == search:
            new_list[index] = replace
    return new_list
