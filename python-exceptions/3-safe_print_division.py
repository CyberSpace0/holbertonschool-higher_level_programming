#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        return None
    finally:
        print(x)
    return x
