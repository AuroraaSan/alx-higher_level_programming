#!/usr/bin/python3

def write_file(filename="", text=""):
    """ reads filename with utf-8 """
    with open(filename, "a", encoding= 'utf-8') as f:
        return f.write(text)