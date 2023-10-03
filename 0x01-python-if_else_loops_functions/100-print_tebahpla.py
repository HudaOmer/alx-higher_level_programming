#!/usr/bin/python3
for i in range(26, -1, -1):
    if i % 2 == 0:
        x = 97
    else:
        x = 65
    print("{}".format(chr(i + x)), end='')
