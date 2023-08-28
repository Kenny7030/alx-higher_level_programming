#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for item in my_list:
        try:
            print("{:d}".format(item), end=" ")
            count += 1
        except (ValueError, TypeError):
            pass  # Skip non-integer values silently

        if count >= x:
            break

    print()  # Print a new line after printing the integers
    return count

