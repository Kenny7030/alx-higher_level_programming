#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count < x:
                print(item, end=" ")
                count += 1
            else:
                break
    except:
        pass  # Handle exceptions without taking any specific action
    finally:
        print()  # Print a new line after printing the elements
    return count

