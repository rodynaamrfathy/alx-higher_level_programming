def add_tuple(tuple_a=(), tuple_b=()):
    add1 = tuple_a[0] if len(tuple_a) > 0 else 0
    add2 = tuple_a[1] if len(tuple_a) > 1 else 0
    add3 = tuple_b[0] if len(tuple_b) > 0 else 0
    add4 = tuple_b[1] if len(tuple_b) > 1 else 0

    result_tuple = (add1 + add3, add2 + add4)
    return result_tuple
