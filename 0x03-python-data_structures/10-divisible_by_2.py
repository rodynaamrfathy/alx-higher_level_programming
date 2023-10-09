#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            check[i] == True
        else:
            check[i] == False
    return check
