#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Counter for the number of integers printed

    try:
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i), end=' ')
                count += 1

            if count == x:  # Break the loop once x integers have been printed
                break

    except:
        pass  # Silently handle any exceptions

    print()  # Print a new line after the integers
    return count
