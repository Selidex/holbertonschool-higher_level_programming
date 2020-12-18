#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    rtoi = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    tot = 0
    i = 0
    while i < len(roman_string):
        a = roman_string[i]
        if (i + 1) != len(roman_string):
            b = roman_string[i + 1]
        else:
            b = 'Z'
        if a is 'C' and b is 'M':
            i += 1
            tot += 900
        elif a is 'C' and b is 'D':
            i += 1
            tot += 400
        elif a is 'X' and b is 'L':
            i += 1
            tot += 40
        elif a is 'X' and b is 'C':
            i += 1
            tot += 90
        elif a is 'I' and b is 'X':
            i += 1
            tot += 9
        elif a is 'I' and b is 'V':
            i += 1
            tot += 4
        else:
            tot += rtoi[a]
        i += 1
    return tot
