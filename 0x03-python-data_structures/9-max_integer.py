#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return "None"
    a = min(my_list)
    for i in range(0, len(my_list)):
        if a < my_list[i]:
            a = my_list[i]
    return a
