#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, count = 0, 0
    for i in range(x):
        try:
            print('{:d}'.format(value))
            count += 1
        except (TypeError, ValueError, IndexError):
            pass
    print()
    return count