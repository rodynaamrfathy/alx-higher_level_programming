#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or (n + 1) >= len(str):
        print("{:s}".format(str))
        return str
    for i in str[i]:
        result = ""
        if i == n:
            continue;
        else:
            result += str[i]