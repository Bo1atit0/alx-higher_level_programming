#!/usr/bin/python3
if __name__ == "__main__":
import sys

lent = len(sys.argv) - 1
if lent == 0:
    print("{} arguments.".format(lent))
elif lent == 1:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(lent))
    for i in range(1, lent+1):
        print("{}: {}".format(i, sys.argv[i]))
