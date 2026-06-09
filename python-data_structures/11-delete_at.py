#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new = my_list
    if idx < 0 or idx >= len(my_list):
        return new

    return new[:idx] + new[idx + 1:]
