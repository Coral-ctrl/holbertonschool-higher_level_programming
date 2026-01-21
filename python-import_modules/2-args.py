#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.\n")
    elif len(argv) == 2:
        print("1 argument:\n")
        print("1: {}".format(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:\n".format(len(argv) - 1))
        for i in range(len(argv)):
            print("{}: {}\n".format(i + 1, argv[i + 1]))
            i += 1
