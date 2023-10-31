#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
ld = num_str[-1]

if number < 0:
    ld = '-' + ld
if int(ld) > 5:
    print("Last digit of", number, "is", ld, "and is greater than 5")
elif int(ld) == 0:
    print("Last digit of", number, "is", ld, "and is 0")
else:
    print("Last digit of", number, "is", ld, "and is less than 6 and not 0")
