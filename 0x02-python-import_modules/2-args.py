#!/usr/bin/python3

import sys
lens = len(sys.argv)
if __name__ == '__main__':

        if len(sys.argv) == 2:
                print(lens - 1, "argument:")
                print("1:",sys.argv[1])
                exit(1)
                
        elif lens == 1:
                print(lens - 1, "arguments:")
                exit(1)

        else:
                print(lens - 1, "arguments:")
                for i, arg in enumerate(sys.argv[1:]):
                        print("{}: {}".format(i + 1,arg))
