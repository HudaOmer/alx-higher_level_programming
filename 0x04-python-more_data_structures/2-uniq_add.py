#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set(my_list)
    sum = 0
    for i in my_list:
        sum += i
    return sum
