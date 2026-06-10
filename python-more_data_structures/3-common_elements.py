#!/usr/bin/python3
def common_elements(set_1, set_2):
    x = []
    for i in set_2:
        if (i in set_1):
            x.append(i)
    return x
