#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while i < x:
            if isinstance(my_list[i], int):
                count += 1
                print("{:d}".format(my_list[i]), end='')
            i += 1
    except(TypeError):
        print("Not of Type Int")
    else:
        print("")
    return count
