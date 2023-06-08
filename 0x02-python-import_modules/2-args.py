#!/usr/bin/python3

import sys
lens = len(sys.argv)
if __name__ == '__main__':
    if lens == 2:
        print(lens - 1, "argument:")

    elif len(sys.argv) > 2:
        print(lens - 1, "arguments:")

    else:
        print(lens - 1, "arguments.")

    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
