#!/usr/bin/python3

import sys

total = 0
for arg in sys.argv[1:]:
    total += int(arg)
if __name__ == "__main__":
    print(total)
