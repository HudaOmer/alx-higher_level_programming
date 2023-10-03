#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 == 0:
        x = 65
    else:
        x = 97
    print("{}".format(chr(i + x)), end='')
