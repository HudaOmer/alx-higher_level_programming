#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a = sorted(a_dictionary.keys())
    return a[len(a) - 1]
