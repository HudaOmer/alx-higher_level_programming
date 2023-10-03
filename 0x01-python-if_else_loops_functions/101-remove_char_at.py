#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    j = 0
    for i in range(0, len(str)):
        if i == n:
            j += 1
            continue
        new = new + str[j]
        j += 1
    return new
