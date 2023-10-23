#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for v in list(a_dictionary.keys()):
        if value == a_dictionary.get(v):
            del a_dictionary[v]
    return (a_dictionary)
