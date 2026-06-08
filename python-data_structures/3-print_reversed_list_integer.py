#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    x = 1
    for i in range(a):
        print("{:d}".format(my_list[a - x]))
        x = x + 1