#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    li = 0
    for n in range(x):
        try:
            print("{}".format(my_list[n]), end="")
            li += 1
        except IndexError:
            break
    print("")
    return (li)
