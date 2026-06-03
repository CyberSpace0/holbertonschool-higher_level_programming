#!/usr/bin/python3
def islower(c):
    check = False
    for i in range(97, 123):
        if (chr(i) == c):
            check = True
            break
    return check

print(islower('c'))