#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add1 = (tuple_b[0] if not tuple_b[0] else 0) + \
    (tuple_a[0] if not tuple_a[0] else 0)
    add2 = (tuple_b[1] if not tuple_b[1] else 0) + \
    (tuple_a[1] if not tuple_a[1] else 0)
    add_tuple = (add1, add2)
