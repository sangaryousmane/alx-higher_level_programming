#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = sum([int(arg) for arg in argv[1:]])
    print("{}".format(total))
