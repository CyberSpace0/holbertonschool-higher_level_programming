#!/usr/bin/python3
def uniq_add(my_list=[]):
    blacklist = []
    result = 0
    for i in my_list:
        if (i in blacklist):
            pass
        else:
            result = result + i
            blacklist.append(i)
    return result
