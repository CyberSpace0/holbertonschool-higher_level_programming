#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) <= 0):
        return None
    a = True
    for i in my_list:
        for x in my_list:
            if (i > x):
                a = True
            else:
                a = False
        if (a == True):
            return i
            break
