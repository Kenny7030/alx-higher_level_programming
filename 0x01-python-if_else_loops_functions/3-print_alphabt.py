#!/usr/bin/python3
# Author - Ken Kariuki
for letter in range(ord('a'), ord('z') + 1):
    if chr(letter) not in ['q', 'e']:
        print("{:c}".format(letter), end="")

