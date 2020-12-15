#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t9 = (0,)
    while (len(tuple_a) < 2):
        tuple_a = tuple_a + t9
    while (len(tuple_b) < 2):
        tuple_b = tuple_b + t9
    if len(tuple_a) > 2:
        tuple_a = tuple_a[0:2]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[0:2]
    return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
