#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Convert each character to uppercase using ASCII manipulation
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
            print("{:c}".format(uppercase_char), end="")
        else:
            print("{:c}".format(char), end="")

    print()  # Print a new line at the end

# Test case
uppercase("Hello, World!")  # Output: HELLO, WORLD!

