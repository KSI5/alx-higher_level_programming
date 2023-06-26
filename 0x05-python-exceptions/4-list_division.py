#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                new_list.append(0)
            else:
                try:
                    result = my_list_1[i] / my_list_2[i]
                    if isinstance(result, (int, float)):
                        new_list.append(result)
                    else:
                        print("wrong type")
                        new_list.append(0)
                except ZeroDivisionError:
                    print("division by 0")
                    new_list.append(0)
        except Exception:
            raise
    return new_list