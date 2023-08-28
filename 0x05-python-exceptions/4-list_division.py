#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError):
            result = 0
            if isinstance(my_list_1[i], str) or isinstance(my_list_2[i], str):
                print(f"Element {i}: Cannot perform division on string.")
            elif my_list_2[i] == 0:
                print(f"Element {i}: Division by zero.")
            else:
                print(f"Element {i}: Index out of range.")
        else:
            n_list.append(result)
    return n_list

