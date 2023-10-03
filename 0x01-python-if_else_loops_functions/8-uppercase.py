#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        s = 0
        if ord(ch) in range(97, 123):
            s = 32
        print("{}".format(ord(ch) - 32), end='')
    print("")
            
