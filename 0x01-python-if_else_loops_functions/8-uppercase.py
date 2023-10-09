#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord("a") <= ord(char) <= ord("z") else char:
            up = chr(ord(char - 32))
        else:
            up = char
        print("{}".format(up), end="")
    print()
