#!/usr/bin/python3

import sys

print(len(sys.argv) - 1, "arguments:")

for i, arg in enumerate(sys.argv[1:]):
    print("{}: {}".format(i + 1,arg))
