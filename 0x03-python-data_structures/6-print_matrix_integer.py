#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        str = " "
        x = len(i)
        for j in range(x):
            if j == x - 1:
                str = ""
            print("{:d}".format(i[j]), end=str)
        print("")
