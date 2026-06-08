#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx > len(my_list) - 1 or idx < 0):
        return my_list
    new = []
    x = 0
    for i in my_list:
        if (idx == x):
            new.append(element)
        else:
            new.append(i)
        x = x + 1
    return new