#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is between the ASCII values of 'a' and 'z'
    return ord('a') <= ord(c) <= ord('z')

# Test cases
print(islower('a'))  # Output: True
print(islower('A'))  # Output: False
print(islower('5'))  # Output: False

