#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cuntr = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            cuntr += 1
    except IndexError:
        pass
    print()
    return cuntr
