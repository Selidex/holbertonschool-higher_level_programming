#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    tot = 0
    wtot = 0
    for i in range(0, len(my_list)):
        tot += int(my_list[i][0]) * int(my_list[i][1])
        wtot += int(my_list[i][1])
    return (tot / wtot)
