#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    element_1 = tuple_a[0] + tuple_b[0]
    element_2 = tuple_a[1] + tuple_b[1]
    return (element_1, element_2)
