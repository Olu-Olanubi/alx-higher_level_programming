#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) != 1 else "argument",
                 "." if (size) == 0 else ":"))
    for i in range(size):
        print("{}: {}".format(i + 1, argv[i+1]))
