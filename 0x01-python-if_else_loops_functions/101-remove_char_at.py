#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for ch in str:
        if ch == str[n]:
            i += 1
            continue
        new[i] = ch
        i += 1
    return new
