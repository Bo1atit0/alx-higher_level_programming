#!/usr/bin/python3
def islower(c):
    #check if c is a lowercase letter by comparing its Unicode code point to the code points of 'a' and 'z'.
    return ord("a") <= ord(c) <= ord("z")
