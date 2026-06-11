#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    try:
        if (key == "" ):
            return a_dictionary
        else:
            dict.pop(a_dictionary,key)
            return a_dictionary
    except:
        return a_dictionary
