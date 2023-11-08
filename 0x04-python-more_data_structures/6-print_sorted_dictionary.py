#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary.items())
    # print(a)
    for key, value in a:
        print("{} : {}".format(key, value))
