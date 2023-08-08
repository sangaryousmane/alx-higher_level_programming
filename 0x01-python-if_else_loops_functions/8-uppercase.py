#!/usr/bin/python3
def islower(c):
    return c in [chr[i] for i in range(97, 123)]

def uppercase(s):
    uppercase_str = ''
    for c in s:
        if islower(c):
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    print("{}".format(uppercase_str))
