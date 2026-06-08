#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx > len(my_list) - 1 or idx < 0):
        return my_list
    new = []
    x = 0
    for i in my_list:
        new[x] = i
        x = x + 1
