#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square._Square__size)  # Access private attribute with name mangling
except Exception as e:
    print(e)

try:
    print(my_square.size)  # This should raise an exception
except Exception as e:
    print(e)

try:
    print(my_square.__size)  # This should raise an exception
except Exception as e:
    print(e)
