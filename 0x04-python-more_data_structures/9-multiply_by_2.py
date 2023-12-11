#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    items = list(a_dictionary.items())
    result = {}
    for key, value in items:
        result[key] = value * 2
    return result
