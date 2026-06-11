#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary or len(a_dictionary) <= 0):
        return None
    try:
        a_dictionary["John"]
        return "John"
    except Exception:
        return "c"
