#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number[-1]
if (last > 5):
    print("Last digit of {:d} is {:d} and {:d} is greater than 5".format(number, last, last))
elif (last == 0):
    print("Last digit of {:d} is {:d} and {:d} is 0".format(number, last, last))
else:
     print("Last digit of {:d} is {:d} and {:d} is less than 6 and not 0".format(number, last, last))