#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    count = len(args)
    i = 0

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    while i in range(count):
        print("{}: {}".format(i + 1, args[i]))
        i += 1
