#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in range(x):
            print("{}".format(my_list[i]), endl='')
            counter += 1
    except IndexError:
        None
    print()
    return counter
