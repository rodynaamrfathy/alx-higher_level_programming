#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        print("{:s}".format(str))
        return str
    result = ""
    for i in str[i]:
        if i == n:
            continue;
        else:
            result += str[i]
