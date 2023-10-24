#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_elm = 0
        for i in range (x):
            print(my_list[i], end="")
            printed_elm += 1
        print()
        return printed_elm
    except:
        return printed_elm