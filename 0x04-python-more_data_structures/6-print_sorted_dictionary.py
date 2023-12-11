#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.keys())
    for key in a:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
