#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for i in list(a_dictionary):
        if i == key:
            # a_dictionary.pop(key)
            del a_dictionary[key]
    return a_dictionary
