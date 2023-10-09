#!/usr/bin/python3
def uppercase(str):
    for char in str:
        up = chr(ord(char - 32))
        print("{}".format(up), end="")
    print()
