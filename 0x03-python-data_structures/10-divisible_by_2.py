#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            div_list.append(True)
        else:
            div_list.append(False)
    return div_list
