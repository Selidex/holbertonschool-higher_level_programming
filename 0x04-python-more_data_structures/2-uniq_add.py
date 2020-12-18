#!/usr/bin/python3
def uniq_add(my_list=[]):
    tot = 0
    test = []
    for x in range(0, len(my_list)):
        if my_list[x] not in test:
            tot += my_list[x]
            test.append(my_list[x])
    return tot
