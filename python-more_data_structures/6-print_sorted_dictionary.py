#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
print_sorted_dictionary({ 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] })