#!/usr/bin/python3
def uppercase(str):
    for char in str:
        up = chr(ord(char - 32)) if ord("a") <= ord(char) <= ord("z") else char
        print("{}".format(up), end="")
    print()
