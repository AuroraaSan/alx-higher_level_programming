#!/usr/bin/python3
""" Functin to add two integers; a and b"""
def add_integer(a, b=98):
    """
    args: 
        a: the first integer
        b: the second integer
    Raises:
        TypeError if a or b aren't integer or float
    Returns:
        result: a + b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")