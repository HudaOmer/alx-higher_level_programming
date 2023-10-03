#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for ch in str:
        if ch == str[n]:
            i++
            continue
        new[i++] = ch
    return new
