#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = 0, 0
    if len(tuple_a) >= 1:
        a += tuple_a[0]
    if len(tuple_b) >= 1:
        a += tuple_b[0]
    if len(tuple_a) >= 2:
        b += tuple_a[1]
    if len(tuple_b) >= 2:
        b += tuple_b[1]
    tuple_new = (a, b)
    return tuple_new
