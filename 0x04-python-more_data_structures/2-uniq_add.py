#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0
    seen_integers = set()
    
    for num in my_list:
        if num not in seen_integers:
            unique_sum += num
            seen_integers.add(num)
    
    return unique_sum
