#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary)
    a.sort()
    for i in a:
        print("{0}: {1}".format(i, a_dictionary[i]))
