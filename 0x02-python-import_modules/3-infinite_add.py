#!/usr/bin/python3
import sys
if __name__ == '__main__':
    total = 0
    num_args = len(sys.argv)
    for arg in sys.argv[1:]:
        if num_args > 1:
            total += int(arg)
    print(total)
