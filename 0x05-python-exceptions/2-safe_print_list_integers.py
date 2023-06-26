#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            try:
                if isinstance(i, int):
                    print("{:d}".format(i), end=" ")
                    count += 1
                if count == x:
                    break
            except:
                pass
    except TypeError:
        pass
    print()
    return count
