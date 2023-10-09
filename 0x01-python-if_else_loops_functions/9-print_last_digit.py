#!/usr/bin/python3
def print_last_digit(number):
    pr = abs(number) % 10
    print("{:d}".format(pr), end= "")
