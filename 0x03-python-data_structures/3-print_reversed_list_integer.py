#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        x = len(my_list)
        for i in range(x):
            print("{:d}".format(my_list[x - i - 1]))
