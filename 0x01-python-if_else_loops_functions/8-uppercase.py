#!/usr/bin/python3
def uppercase(str):
    for s in str:
        up = chr(ord(s - 32))
        print("{}".format(up), end="")
    print()
