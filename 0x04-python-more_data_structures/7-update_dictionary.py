#!/bin/usr/python3
def update_dictionary(a_dictionary, key, value):
    b_dictionary = {key: value}
    a_dictionary.update(b_dictionary)
    return a_dictionary
