#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
if last > 5:
    print(f"Last digit of {number} is {last} and {last} is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and {last} is 0")
else:
    print(f"Last digit of {number} is {last} and {last} is less than 5 and not 0")
