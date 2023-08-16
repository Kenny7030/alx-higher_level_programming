#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_arguments = len(argv)

    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num_arguments))

    for i, arg in enumerate(argv, start=1):
        print("{:d}: {}".format(i, arg))

